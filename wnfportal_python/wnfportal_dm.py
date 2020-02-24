#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import cherrypy
import json
import datetime
import wnfportal_dm_konten
import wnfportal_dm_adressen
import wnfportal_dm_termine
import wnfportal_tools as T


class object_q(object):
  def is_angemeldet(self):
    return True

  @cherrypy.expose
  def konten(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      j = k.jsonAlleKonten()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def kontenhtml(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      summe = T.sDM(k.summeAlleKonten())
      s = ''
      for l in k.listeAlleKonten():
        konto = l['konto']  # .encode('utf-8')
        saldo = l['saldo']
        # print type(konto),konto
        s = '%s <tr><td class=table-left>%s</td><td class=table-right-currency>%s</td></tr>' % (s, konto, saldo)
        # s = konto
        # print s
      # s='<tr><td class=table-left>bb</td><td class=table-right-currency>aa</td></tr>'
      s = ("<table>"
           "<tr><th class=table-left>Konto</th><th class=table-right-currency>Stand</th></tr>"
           "%s"
           "<tr><th class=table-left>Summe</th><th class=table-right-currency>%s</th></tr>"
           "</table>") % (s, summe)
      summe = T.sDM(k.summeProjektWintergarten())
      s = ("%s"
           "<table>"
           "<tr><th class=table-left><a href=/projektWintergarten2017 >Projekt Wintergarten 2017</a></th><th class=table-right-currency>%s</th></tr>"
           "</table>") % (s, summe)
      k.closeConnection
      return s
    else:
      return ""

  @cherrypy.expose
  def konten_ea(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      j = k.jsonLetzteEA()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def konten_list_ea(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      j = k.jsonListEA()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def konten_list_ea_skip(self, aFirst, aSkip):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      j = k.jsonListEASkip(aFirst, aSkip)
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def konten_kontostand(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      j = k.jsonListKonten()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def konten_kontostandSumme(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      j = k.jsonKontostandSumme()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def kontostand(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      j = k.jsonAlleKonten()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def konten_detail_ea(self, id):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      j = k.jsonDetailEA(id)
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def konten_ea_html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmlLetzteEA()
      return t
    else:
      return ''

  def konten_ea_monatlich_html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmlEAMonatlich()
      return t
    else:
      return ''

  @cherrypy.expose
  def diagrammLetzterMonat_html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmldiagrammLetzterMonat()
      return t
    else:
      return ''

  @cherrypy.expose
  def diagrammKontoVerlauf_html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmldiagrammKontoVerlauf()
      return t
    else:
      return ''

  @cherrypy.expose
  def diagrammLetzte12Monate_html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmldiagrammLetzte12Monate()
      return t
    else:
      return ''

  @cherrypy.expose
  def diagrammDieserMonat_html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmldiagrammDieserMonat()
      return t
    else:
      return ''

  @cherrypy.expose
  def konten_allejahre(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      j = k.jsonAlleJahreEA()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def konten_allejahre_html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmlAlleJahreEA()
      # print t
      return t
    else:
      return ""

  @cherrypy.expose
  def konten_allemonate_html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmlAlleMonateEA()
      # print t
      return t
    else:
      return ""

  @cherrypy.expose
  def einkommen_allemonate_html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmlAlleMonateEinkommen()
      # print t
      return t
    else:
      return ""

  @cherrypy.expose
  def einkommen_allemonate_chartjs(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.chartjsAlleMonateEinkommen()
      # print t
      return t
    else:
      return ("","","")

  @cherrypy.expose
  def einkommen_allejahre_chartjs(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.chartjsAlleJahreEinkommen()
      # print t
      return t
    else:
      return ("","","")

  @cherrypy.expose
  def projektWintergarten2017html(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmlProjektWintergarten2017()
      # print t
      return t
    else:
      return ""

  @cherrypy.expose
  def projektWintergarten2017htmlK(self):
    if self.is_angemeldet():
      k = wnfportal_dm_konten.dmKonten()
      t = k.htmlProjektWintergarten2017K()
      # print t
      return t
    else:
      return ""

  @cherrypy.expose
  def konten_test(self):
    if self.is_angemeldet():
      j = {'summe': 1000,
           'konten': [
             {'konto': 'Giro', 'saldo': -2000},
             {'konto': 'Sparbuch', 'saldo': 3000}
           ]
           }
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def aufgaben(self):
    if self.is_angemeldet():
      a = wnfportal_dm_adressen.dmAdressen()
      j = a.jsonAlleAufgaben()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def adressen(self):
    if self.is_angemeldet():
      a = wnfportal_dm_adressen.dmAdressen()
      j = a.jsonAlleAdressen()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def adrtop10(self):
    if self.is_angemeldet():
      a = wnfportal_dm_adressen.dmAdressen()
      j = a.jsonTop10Adressen()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def adrdetails(self, aID):
    # print aID
    if self.is_angemeldet():
      a = wnfportal_dm_adressen.dmAdressen()
      j = a.jsonEineAdresse(aID)
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def aufgaben_test(self):
    if self.is_angemeldet():
      j = {'anzahl': 1000,
           'aufgaben': [
             {'aufgabe': 'Sofort', 'prio': 9},
             {'aufgabe': 'Nie', 'prio': 0}
           ]
           }
      return json.dumps(j)
    else:
      return json.dumps({})

  @cherrypy.expose
  def termine(self):
    if self.is_angemeldet():
      k = wnfportal_dm_termine.dmTermine()
      j = k.jsonAlleTermine()
      # print j
      return json.dumps(j)
    else:
      return json.dumps({})
