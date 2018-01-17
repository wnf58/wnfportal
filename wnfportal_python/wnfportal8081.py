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
from wnfportal_dm import object_q

ENTWICKLUNG = True


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
  c['/'] = {'tools.staticdir.on': True, 'tools.staticdir.dir': "www", 'tools.staticdir.index': "index.html"}
  # c['/']={'tools.staticdir.on':True,'tools.staticdir.dir':"m",'tools.staticdir.index' : "index.html"}
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
       '   <link rel="stylesheet" href="css/wnfportal.css"/>'
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
    print(dir(self.q))

  def index(self):
    k = wnfHTMLKopf('', 'wnfPortal')
    b = (
      "<h2>Adressen</h2>"
      "<h2>Finanzen</h2>"
      "<ul>"
      "  <li><a href=kontostand>Kontostand</a></li>"
      "  <li><a href=kontostandAlleJahre>Kontostand alle Jahre</a></li>"
      "  <li><a href=kontostandLetzterMonat>Kontostand Letzter Monat</a></li>"
      "  <li><a href=projektWintergarten2017>Projekt Wintergarten 2017</a></li>"
      "</ul>"
    )
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  index.exposed = True

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

  def kontostandLetzterMonat(self):
    k = wnfHTMLKopf('E/A Letzter Monat', 'E/A Letzter Monat')
    b = self.q.konten_ea_html()
    f = wnfHTMLFuss()
    return "%s%s%s" % (k, b, f)

  kontostandLetzterMonat.exposed = True

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

  def jsonDetailEA(self,id):
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


def CORS():
  cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


def main():
  cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
  cherrypy.quickstart(wnfPortal(), config=server_dict())
  return 0


if __name__ == '__main__':
  main()
