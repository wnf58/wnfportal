from bottle import route, get, post, request, template, HTTPResponse, static_file

import os
import fdb
import time

import wnfportal_const as C
import wnfportal_dm_konten2

www = os.path.join(os.path.dirname(__file__), 'www')


def keinZugriff(daten):
  s = ('Kein Zugriff %s (Serverzeit %s)' % (C.PROGBUILD, (time.strftime("%d.%m.%Y %H:%M:%S"))))
  return template('<b>Hello {{name}}!</b><hr>{{meldung}}', name=daten, meldung=s)


def startseite():
  b = (
    "<h1>wnfPortal</h1>"
    "<hr>"
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
  return b


@get('/kontostandLetzterMonat')
def kontostandLetzterMonat():
  aCaption = "%s.%d E/A Letzter Monat" % (C.PROGNAME, C.PROGBUILD)
  k = wnfportal_dm_konten2.dmKonten()
  rows = k.rowsLetzteEA()
  output = template('tpl_ea',
                    title=aCaption,
                    wnfPortalDaten=rows
                    )
  return output


@get('/kategorie_ea/<kat_id>')
def kategorie_ea(kat_id):
  aCaption = "%s.%d E/A Kategorie %s" % (C.PROGNAME, C.PROGBUILD, kat_id)
  k = wnfportal_dm_konten2.dmKonten()
  rows = k.rowsKategorieEA(kat_id)
  output = template('tpl_ea',
                    title=aCaption,
                    wnfPortalDaten=rows
                    )
  return output

@get('/kostenstelle_ea/<kst_id>')
def kostenstelle_ea(kst_id):
  aCaption = "%s.%d E/A Kostenstelle %s" % (C.PROGNAME, C.PROGBUILD, kst_id)
  k = wnfportal_dm_konten2.dmKonten()
  rows = k.rowsKostenstelleEA(kst_id)
  output = template('tpl_ea',
                    title=aCaption,
                    wnfPortalDaten=rows
                    )
  return output



@get("/css/<filepath:re:.*\.css>")
def css(filepath):
  return static_file(filepath, root=os.path.join(www, "css"))


@get("/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
  return static_file(filepath, root=os.path.join(www, "img"))


@get("/js/<filepath:re:.*\.js>")
def js(filepath):
  return static_file(filepath, root=os.path.join(www, "js"))


@route('/')
def index():
  return startseite()


def startBottle():
  from bottle import run, debug
  debug(True)
  aPortClient = 8082
  run(host='0.0.0.0', port=aPortClient)


def main():
  startBottle()


if __name__ == "__main__":
  main()
