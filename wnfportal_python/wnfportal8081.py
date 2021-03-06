#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

#  wnfportal.py
#
#  Copyright 2014 Uwe Wilske KiDO <wnf@c2012>
#
#  http://halvar.at/python/cherrypy_cheetah/#was-wird-von-cherrypy-bei-welchem-url-ausgeliefert

import os
import cherrypy
import json
from bottle import template

from wnfportal_dm import object_q
import wnfportal_dm_konten

ENTWICKLUNG = True

www = os.path.join(os.path.dirname(os.path.abspath(__file__)),'www')

# Dict zur Steuerung des Servers
def server_dict():
  '''Erstellung der Konfiguration für CherryPy'''
  g = {}
  g['tools.staticdir.root'] = os.path.dirname(os.path.abspath(__file__))
  g['server.socket_port'] = 8081
  g['server.socket_host'] = '0.0.0.0'
  g['tools.sessions.on'] = True
  g['tools.sessions.timeout'] = 1000
  g['tools.sessions.name'] = "wnfportal8081id"
  g['tools.CORS.on'] = True
  if ENTWICKLUNG:
    g['tools.sessions.storage_type'] = "File"
    g['tools.sessions.storage_path'] = '/tmp/'
  else:
    g['environment'] = "production"
  c = {'global': g}
  c['/'] = {'tools.staticdir.on': True,
            'tools.staticdir.dir': "www",
            'tools.staticdir.index': "index.html"}
  # c['/']={'tools.staticdir.on':True,'tools.staticdir.dir':"m",'tools.staticdir.index' : "index.html"}
  # für put-Anweisungen
  c['/put_url'] = {'tools.response_headers.on': True,
                   'tools.response_headers.headers': [('Content-Type', 'text/plain')]}
  return c


def wnfHTMLKopf(aTitle, aCaption):
  s = ('<html>'
       '<head>'
       '   <title>wnfPortal %s</title>'
       '   <meta charset="UTF-8">'
       '   <meta name="viewport" content="width=device-width, initial-scale=1">'
       '   <meta name="apple-mobile-web-app-capable" content="yes" />'
       '   <meta name="apple-mobile-web-app-status-bar-style" content="black" />'
       '   <link rel="apple-touch-startup-image" href="img/wnfPortal.png" />'
       '   <link rel="stylesheet" href="css/wnfportal_2.css"/>'
       '</head>'
       '<body>'
       '<h1>%s</h1>')
  s = s % (aTitle, aCaption)
  return s


def wnfHTMLFuss():
  s = ("<a href=index>zurück</a>"
       "</body>"
       "</html>")
  return s


class wnfPortal(object):
  def __init__(self):
    self.q = object_q()
    #print(dir(self.q))

  def index(self):
    k = wnfHTMLKopf('', 'wnfPortal')
    b = (
      "<h2>Adressen</h2>"
      "<h2>Finanzen</h2>"
      "<ul>"
      "  <li><a href=kontostand>Kontostand</a></li>"
      "  <li><a href=kontostandLetzterMonat>E/A Letzter Monat</a></li>"
      "  <li><a href=eaMonatlich>E/A Statistik monatlich</a></li>"
      "  <li><a href=kontostandAlleJahre>Kontostand alle Jahre</a></li>"
      "  <li><a href=kontostandAlleMonate>Kontostand alle Monate</a></li>"
      "  <li><a href=einkommenAlleMonate>Einkommen alle Monate</a></li>"
      "  <li><a href=einkommenAlleJahre>Einkommen alle Jahre</a></li>"
      "  <li><a href=projektWintergarten2017>Projekt Wintergarten 2017</a></li>"
      "  <li><a href=chartKontoVerlauf>Diagramm Kontoverlauf</a></li>"
      "  <li><a href=diagrammLetzterMonat>Diagramm letzter Monat</a></li>"
      "  <li><a href=diagrammLetzte12Monate>Diagramm letzte 12 Monate</a></li>"
      "  <li><a href=diagrammDieserMonat>Diagramm dieser Monat</a></li>"
      "</ul>"
    )
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  index.exposed = True

  def updater(self, data):
    cherrypy.log.error("hello")
    cherrypy.log.error(data)
    return "The data {} has been puted".format(data)

  updater.exposed = True

  def kontostand(self):
    k = wnfHTMLKopf('Kontostand', 'Kontostand')
    b = self.q.kontenhtml()
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  kontostand.exposed = True

  def kontostandAlleJahre(self):
    k = wnfHTMLKopf('Kontostand alle Jahre', 'Kontostand alle Jahre')
    b = self.q.konten_allejahre_html()
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  kontostandAlleJahre.exposed = True

  def kontostandAlleMonate(self):
    k = wnfHTMLKopf('Kontostand alle Monate', 'Kontostand alle Monate')
    b = self.q.konten_allemonate_html()
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  kontostandAlleMonate.exposed = True

  def charttpl(self,aUeberschrift,aLabels,aEKU,aEKS):
    #print(aLabels)
    aCaption = aUeberschrift
    output = template('chart.tpl',
                      title=aCaption,
                      Ueberschrift=aUeberschrift,
                      Labels=(aLabels),
                      EKU=aEKU,
                      EKS=aEKS
                      )
    return output

  def einkommenAlleMonate(self):
    aLabels,aEKU,aEKS = self.q.einkommen_allemonate_chartjs()
    t = self.charttpl('Einkommen alle Monate',aLabels,aEKU,aEKS)
    return t

  einkommenAlleMonate.exposed = True

  def einkommenAlleJahre(self):
    aLabels,aEKU,aEKS = self.q.einkommen_allejahre_chartjs()
    t = self.charttpl('Einkommen alle Jahre',aLabels,aEKU,aEKS)
    return t

  einkommenAlleJahre.exposed = True


  def kontostandLetzterMonat(self):
    k = wnfHTMLKopf('E/A Letzter Monat', 'E/A Letzter Monat')
    b = self.q.konten_ea_html()
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  kontostandLetzterMonat.exposed = True

  def eaMonatlich(self):
    k = wnfHTMLKopf('E/A monatlich', 'E/A monatlich')
    b = self.q.konten_ea_monatlich_html()
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  eaMonatlich.exposed = True

  def diagrammLetzterMonat(self):
    k = wnfHTMLKopf('Ausgaben letzter Monat', 'Ausgaben letzter Monat')
    b = self.q.diagrammLetzterMonat_html()
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  diagrammLetzterMonat.exposed = True

  def diagrammKontoVerlauf(self):
    dn = os.path.join(www,'daten','kontoverlauf.csv')
    k = wnfportal_dm_konten.dmKonten()
    k.csvKontoVerlauf(dn)
    output = template('konto_verlauf',
                      title='Kontoverlauf'
                      )
    return output

  diagrammKontoVerlauf.exposed = True

  def chartKontoVerlauf(self):
    k = wnfportal_dm_konten.dmKonten()
    aLabels,aDaten = k.chartjsKontoverlauf()
    output = template('chart_linie',
                      title='wnfPortal - Kontoverlauf',
                      Ueberschrift='Kontoverlauf',
                      Labels=aLabels,
                      Daten=aDaten
                      )
    return output

  chartKontoVerlauf.exposed = True

  def diagrammLetzte12Monate(self):
    k = wnfHTMLKopf('Ausgaben letzte 12 Monate', 'Ausgaben letzte 12 Monate')
    b = self.q.diagrammLetzte12Monate_html()
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  diagrammLetzte12Monate.exposed = True

  def diagrammDieserMonat(self):
    k = wnfHTMLKopf('Ausgaben dieser Monat', 'Ausgaben dieser Monat')
    b = self.q.diagrammDieserMonat_html()
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  diagrammDieserMonat.exposed = True

  def projektWintergarten2017(self):
    k = wnfHTMLKopf('Projekt Wintergarten 2017', 'Projekt Wintergarten 2017')
    l = "<strong>einzeln</strong> <a href=projektWintergarten2017K>gruppiert</a>"
    b = self.q.projektWintergarten2017html()
    f = wnfHTMLFuss()
    return "%s%s%s%s" % (k, l, b, f)

  projektWintergarten2017.exposed = True

  def projektWintergarten2017K(self):
    k = wnfHTMLKopf('Projekt Wintergarten 2017', 'Projekt Wintergarten 2017')
    l = "<a href=projektWintergarten2017>einzeln</a> <strong>gruppiert</<strong>"
    b = self.q.projektWintergarten2017htmlK()
    f = wnfHTMLFuss()
    return "%s%s%s%s" % (k, l, b, f)

  projektWintergarten2017K.exposed = True

  def jsonListEA(self):
    j = self.q.konten_list_ea()
    return j

  jsonListEA.exposed = True

  def jsonListEASkip(self,aFirst, aSkip):
    j = self.q.konten_list_ea_skip(aFirst,aSkip)
    return j

  jsonListEASkip.exposed = True

  def jsonDetailEA(self, id):
    j = self.q.konten_detail_ea(id)
    return j

  jsonDetailEA.exposed = True

  def jsonKontostand(self):
    j = self.q.konten_kontostand()
    return j

  jsonKontostand.exposed = True

  def jsonKontostandSumme(self):
    j = self.q.konten_kontostandSumme()
    return j

  jsonKontostandSumme.exposed = True

  @cherrypy.expose
  def submit(self, name):
    # print(name)
    k = [{'title': name}]
    j = json.dumps(k)
    return j
    cherrypy.response.headers['Content-Type'] = 'application/json'
    return json.dumps(dict(title="Hello, %s" % name))


def CORS():
  cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


def main():
  cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
  webapp = wnfPortal()
  cherrypy.quickstart(webapp, config=server_dict())
  return 0


if __name__ == '__main__':
  main()
