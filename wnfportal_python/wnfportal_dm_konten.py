#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import fdb
import os
import configparser
import wnfportal_dm_datenbank
import wnfportal_tools as T

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import renderPM


class dmKonten(wnfportal_dm_datenbank.dmDatenbank):
  def __init__(self):
    wnfportal_dm_datenbank.dmDatenbank.__init__(self)
    self.setIniDatei('wnfKuB.ini')
    # self.setIniDatei('wnfKITAOffice.ini')

  def summeAlleKonten(self):
    aSQL = """
          SELECT SUM(BETRAG) FROM KO_KUBEA
          """
    return self.sqlSumme(aSQL)

  def summeProjekt(self, aProjekt_ID):
    aSQL = "SELECT SUM(BETRAG) FROM KO_KUBEA WHERE PROJEKT_ID=%s" % (aProjekt_ID)
    print(aSQL)
    return self.sqlSumme(aSQL)

  def summeProjektWintergarten(self):
    aProjekt_ID = self.getProjekt_ID_Wintergarten_2017()
    return self.summeProjekt(aProjekt_ID)

  def listeAlleKonten(self):
    aSQL = """
            SELECT E.KUB_ID,K.KURZ,SUM(E.BETRAG)
            FROM KO_KUBEA E
            LEFT JOIN KO_KUB K ON K.ID=E.KUB_ID
            GROUP BY K.KURZ,E.KUB_ID
            HAVING SUM(E.BETRAG)<>0
            ORDER BY K.KURZ
          """
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return []
    konten = []
    for row in cur:
      k = {'konto_id': row[0], 'konto': row[1], 'saldo': T.sDM(row[2])}
      # print k
      konten.append(k)
    return konten

  def jsonAlleKonten(self):
    j = {'summe': T.sDM(self.summeAlleKonten()), 'konten': self.listeAlleKonten()}
    return j

  def listeLetzteEA(self):
    aSumme = 0
    aSQL = """
            SELECT E.ID,E.DATUM,E.KURZ,E.BETRAG
            FROM KO_KUBEA E
            WHERE E.DATUM >= %s
            ORDER BY E.DATUM DESC,E.KURZ
          """
    aSQL = aSQL % (T.wnfDateToSQL(T.wnfErsterTagVormonat()))
    print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return aSumme, []
    ea = []
    for row in cur:
      s = "%s | %s" % (row[1].strftime("%d.%m.%y"), row[2])
      ttmmjj = "%s" % (row[1].strftime("%d.%m.%y"))
      # print (s)
      k = {'konto_ea_id': row[0],
           'datum': str(row[1]),
           'ttmmjj': ttmmjj,
           'kurz': row[2],
           'betrag': T.sDM(row[3]),
           'datumkurz': s}
      aSumme = aSumme + row[3]
      print(k)
      ea.append(k)
    return aSumme, ea

  def listeProjekt(self, aProjekt_ID):
    print(aProjekt_ID)
    aSumme = 0
    aSQL = """
            SELECT E.ID,E.DATUM,E.KURZ,E.BETRAG
            FROM KO_KUBEA E
            WHERE E.PROJEKT_ID = %d
            ORDER BY E.DATUM DESC,E.KURZ
          """
    aSQL = aSQL % (aProjekt_ID)
    print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return aSumme, []
    ea = []
    for row in cur:
      s = "%s | %s" % (row[1].strftime("%d.%m.%y"), row[2])
      ttmmjj = "%s" % (row[1].strftime("%d.%m.%y"))
      # print (s)
      k = {'konto_ea_id': row[0],
           'datum': str(row[1]),
           'ttmmjj': ttmmjj,
           'kurz': row[2],
           'betrag': T.sDM(row[3]),
           'datumkurz': s}
      aSumme = aSumme + row[3]
      print(k)
      ea.append(k)
    return aSumme, ea

  def listeProjektK(self, aProjekt_ID):
    print(aProjekt_ID)
    aSumme = 0
    aSQL = """
            SELECT K.ID,MAX(E.DATUM),K.KURZ,SUM(E.BETRAG)
            FROM KO_KUBEA E
            LEFT JOIN KO_KUBKAT K ON K.ID=E.KAT_ID
            WHERE E.PROJEKT_ID = %d
            AND NOT E.KAT_ID IS NULL
            GROUP BY K.ID,K.KURZ 
            ORDER BY 4,K.KURZ
          """
    aSQL = aSQL % (aProjekt_ID)
    print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return aSumme, []
    ea = []
    for row in cur:
      s = "%s | %s" % (row[1].strftime("%d.%m.%y"), row[2])
      ttmmjj = "%s" % (row[1].strftime("%d.%m.%y"))
      # print (s)
      k = {'konto_ea_id': row[0],
           'datum': str(row[1]),
           'ttmmjj': ttmmjj,
           'kurz': row[2],
           'betrag': T.sDM(row[3]),
           'datumkurz': s}
      aSumme = aSumme + row[3]
      print(k)
      ea.append(k)
    return aSumme, ea

  def jsonLetzteEA(self):
    aSumme, ea = self.listeLetzteEA()
    j = {'summe': T.sDM(aSumme), 'ea': ea}
    return j

  def jsonListEA(self):
    aSQL = """
            SELECT E.ID,E.DATUM,E.KURZ, E.BEZ, E.BETRAG
            FROM KO_KUBEA E
            WHERE E.DATUM >= %s
            ORDER BY E.DATUM DESC,E.KURZ
          """
    aSQL = aSQL % (T.wnfDateToSQL(T.wnfErsterTagVormonat()))
    # print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return []
    ea = []
    for row in cur:
      s = "%s | %s" % (row[1].strftime("%d.%m.%y"), row[2])
      ttmmjj = "%s" % (row[1].strftime("%d.%m.%y"))
      # print s
      k = {'id': row[0],
           'datum': str(row[1]),
           'kurz': row[2],
           'bez': row[3],
           'betrag': str(row[4])}
      # print(k)
      ea.append(k)
    # print(ea)
    return ea

  def jsonListEASkip(self, aFirst, aSkip):
    aSQL = """
              SELECT FIRST %s SKIP %s E.ID,E.DATUM,E.KURZ, E.BEZ, E.BETRAG
              FROM KO_KUBEA E
              ORDER BY E.DATUM DESC,E.KURZ
            """
    aSQL = aSQL % (aFirst, aSkip)
    # print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return []
    ea = []
    for row in cur:
      s = "%s | %s" % (row[1].strftime("%d.%m.%y"), row[2])
      ttmmjj = "%s" % (row[1].strftime("%d.%m.%y"))
      # print s
      k = {'id': row[0],
           'datum': str(row[1]),
           'kurz': row[2],
           'bez': row[3],
           'betrag': str(row[4])}
      # print(k)
      ea.append(k)
    print(ea)
    return ea

  def jsonDetailEA(self, id):
    aSQL = """
            SELECT E.ID,E.DATUM,E.KURZ, E.BEZ, E.BETRAG
            FROM KO_KUBEA E
            WHERE E.ID = %s
            ORDER BY E.DATUM DESC,E.KURZ
          """
    aSQL = aSQL % (id)
    # print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return []
    for row in cur:
      s = "%s | %s" % (row[1].strftime("%d.%m.%y"), row[2])
      ttmmjj = "%s" % (row[1].strftime("%d.%m.%y"))
      # print s
      k = {'id': row[0],
           'datum': str(row[1]),
           'kurz': row[2],
           'bez': row[3],
           'betrag': str(row[4])}
      print(k)
      return k

  def jsonListKonten(self):
    aSQL = """
            SELECT 
              K.ID,
              MAX(E.DATUM),
              K.KURZ,
              SUM(E.BETRAG)
            FROM KO_KUBEA E
            LEFT JOIN KO_KUB K ON K.ID=E.KUB_ID
            GROUP BY K.KURZ,K.ID
            HAVING SUM(E.BETRAG)<>0
            ORDER BY K.KURZ
          """
    # print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return []
    ea = []
    for row in cur:
      k = {'id': row[0],
           'datum': str(row[1]),
           'kurz': row[2],
           'betrag': str(row[3])}
      # print(k)
      ea.append(k)
    print(ea)
    return ea

  def jsonKontostandSumme(self):
    aSQL = """
            SELECT 
              SUM(E.BETRAG)
            FROM KO_KUBEA E
          """
    # print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return {}
    for row in cur:
      k = [{'summe': str(row[0])}]
      print(k)
      return k

  def htmlLetzteEA(self):
    aSumme, ea = self.listeLetzteEA()
    s = ''
    for l in ea:
      datum = l['ttmmjj']  # .encode('utf-8')
      kurz = l['kurz']  # .encode('utf-8')
      betrag = l['betrag']
      s = '%s <tr><td class=table-3c-spalte1>%s</td><td class=table-3c-spalte2>%s</td><td class=table-3c-spalte3>%s</td></tr>' % (
        s, datum, kurz, betrag)
    return ("<table>"
            "<tr><th class=table-3c-spalte1>Datum</th><th class=table-3c-spalte2>Bezeichnung</th><th class=table-3c-spalte3>Betrag</th></tr>"
            "%s"
            "<tr><th class=table-3c-spalte1></th><th class=table-3c-spalte2>Summe</th><th class=table-3c-spalte3>%s</th></tr>"
            "</table>") % (s, T.sDM(aSumme))

  def htmldiagrammLetzterMonat(self):
    aVon = T.wnfDateToSQL(T.wnfErsterTagVormonat())
    aBis = T.wnfDateToSQL(T.wnfLetzterTagVormonat())
    aSumme, aData, aLabels, aRecord = self.analyseAusgabenVonBis(aVon, aBis)
    p = '/home/wnf/Entwicklung/PycharmProjects/wnfportal/wnfportal_python/www/img/'
    dn = 'kreis_vormonat'
    self.diagrammKostenartVonBis(p, dn, aData, aLabels)
    s = ''
    for l in aRecord:
      aLabel = l['ID']
      kurz = l['kurz']  # .encode('utf-8')
      betrag = l['sDM']
      s = '%s <tr><td class=table-3c-spalte1>%s</td><td class=table-3c-spalte2>%s</td><td class=table-3c-spalte3>%s</td></tr>' % (
        s, aLabel, kurz, betrag)
    tabelle = ("<table>"
               "<tr><th class=table-3c-spalte1>Kurz</th><th class=table-3c-spalte2>Bezeichnung</th><th class=table-3c-spalte3>Betrag</th></tr>"
               "%s"
               "<tr><th class=table-3c-spalte1></th><th class=table-3c-spalte2>Summe</th><th class=table-3c-spalte3>%s</th></tr>"
               "</table>") % (s, T.sDM(aSumme))
    return ('<img src="img/%s.png" alt="Diagramm"> %s' % (dn, tabelle))

  def listeAlleJahreEA(self):
    aSumme = 0
    aAnzJahre = 0
    aSQL = """
            SELECT
            EXTRACT(YEAR FROM E.DATUM) AS JAHR,
            SUM(E.BETRAG),
            SUM(CASE WHEN E.BETRAG > 0 THEN E.BETRAG END) AS Einnahme, 
            SUM(CASE WHEN E.BETRAG < 0 THEN E.BETRAG END) AS Ausgabe 
            FROM KO_KUBEA E
            WHERE E.IGNORIEREN = 0
            GROUP BY EXTRACT(YEAR FROM E.DATUM)
            ORDER BY 1 DESC
          """
    # print aSQL
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return aSumme, []
    ea = []
    for row in cur:
      s = "%s | %20s" % (row[0], T.sDM(row[1]))
      # print s
      k = {'jahr': row[0],
           'betrag': row[1],
           'sDM': T.sDM(row[1]),
           'sDME': T.sDM(row[2]),
           'sDMA': T.sDM(row[3])
           }
      aSumme = aSumme + row[1]
      aAnzJahre = aAnzJahre + 1
      # print k
      ea.append(k)
    if aAnzJahre > 0:
      aSumme = aSumme / aAnzJahre
    return aAnzJahre, aSumme, ea

  def listeKostenartVonBis(self, aVon, aBis):
    aSQL = """
      SELECT ABS(SUM(E.BETRAG)),K.KURZ,K.ID 
      FROM KO_KUBEA E
      LEFT JOIN KO_KUBKST K ON K.ID=E.KST_ID
      WHERE E.IGNORIEREN = 0
      AND NOT E.KST_ID IS NULL
      AND E.BETRAG < 0
      AND E.DATUM BETWEEN %s AND %s
      GROUP BY K.KURZ,K.ID
      ORDER BY 2
      """
    aSQL = aSQL % (aVon, aBis)
    print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return [], []
    ea = []
    kst = []
    aRecord = []
    aSumme = 0
    for row in cur:
      # s = "%s | %20s" % (row[0], T.sDM(row[1]))
      # print s
      ea.append(round(row[0]))
      aSumme = aSumme + row[0]
      kst.append(row[1])
      k = {'betrag': row[0],
           'sDM': T.sDM(row[0]),
           'kurz': row[1],
           'ID': row[2]
           }
      # print(aSumme)
      aRecord.append(k)

    return aSumme, ea, kst, aRecord

  def analyseAusgabenVonBis10Prozent(self, aKst_ID, aVon, aBis, a10Prozent):
    aSQL = """
        SELECT SUM(ABS(E.BETRAG)),K.KURZ,K.ID 
        FROM KO_KUBEA E
        LEFT JOIN KO_KUBKAT K ON K.ID=E.KAT_ID
        WHERE E.IGNORIEREN = 0
        AND E.KST_ID = %d
        AND E.BETRAG < 0
        AND E.DATUM BETWEEN %s AND %s
        GROUP BY K.KURZ,K.ID
        ORDER BY 2
        """
    aSQL = aSQL % (aKst_ID, aVon, aBis)
    print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return []
    aRec = []
    for row in cur:
      x = {'betrag': row[0],
           'sDM': T.sDM(row[0]),
           'kurz': row[1],
           'ID': aKst_ID
           }
      aRec.append(x)
    return aRec

  def analyseAusgabenVonBis(self, aVon, aBis):
    """
    Alle EA bis 10 % zusammenfassen
    """
    aSQL = """
      SELECT ABS(SUM(E.BETRAG)),K.KURZ,K.ID 
      FROM KO_KUBEA E
      LEFT JOIN KO_KUBKST K ON K.ID=E.KST_ID
      WHERE E.IGNORIEREN = 0
      AND NOT E.KST_ID IS NULL
      AND E.BETRAG < 0
      AND E.DATUM BETWEEN %s AND %s
      GROUP BY K.KURZ,K.ID
      ORDER BY 2
      """
    aSQL = aSQL % (aVon, aBis)
    print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return 0, [], [], []
    ea = []
    kst = []
    aRecord = []
    aRecKst = []
    aSumme = 0
    for row in cur:
      # s = "%s | %20s" % (row[0], T.sDM(row[1]))
      # print s
      k = {'betrag': row[0],
           'kurz': row[1],
           'KST_ID': row[2]
           }
      aSumme = aSumme + row[0]
      # print(aSumme)
      aRecKst.append(k)
    a10Prozent = aSumme / 10
    print(aSumme, a10Prozent)

    for k in aRecKst:
      if (k['betrag'] < a10Prozent):
        x = {'betrag': k['betrag'],
             'sDM': T.sDM(k['betrag']),
             'kurz': k['kurz'],
             'ID': k['KST_ID']
             }
        aRecord.append(x)
      else:
        rx = self.analyseAusgabenVonBis10Prozent(k['KST_ID'], aVon, aBis, a10Prozent)
        for x in rx:
          aRecord.append(x)
    print(aRecord)
    for x in aRecord:
      ea.append(round(x['betrag']))
      kst.append(x['kurz'])
    print(kst)
    print(ea)
    return aSumme, ea, kst, aRecord

  def listeAlleMonateEA(self):
    aSumme = 0
    aAnzMonate = 0
    aSQL = """
            SELECT
            EXTRACT(YEAR FROM E.DATUM) AS JAHR,
            EXTRACT(MONTH FROM E.DATUM) AS MONAT,
            SUM(E.BETRAG),
            SUM(CASE WHEN E.BETRAG > 0 THEN E.BETRAG END) AS Einnahme, 
            SUM(CASE WHEN E.BETRAG < 0 THEN E.BETRAG END) AS Ausgabe 
            FROM KO_KUBEA E
            WHERE E.IGNORIEREN = 0
            GROUP BY EXTRACT(YEAR FROM E.DATUM),EXTRACT(MONTH FROM E.DATUM)
            ORDER BY 1 DESC,2 DESC
          """
    # print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return aAnzMonate, aSumme, []
    ea = []
    for row in cur:
      s = "%s | %20s" % (row[0], T.sDM(row[1]))
      # print s
      k = {'jahr': row[0],
           'monat': row[1],
           'betrag': row[2],
           'sDM': T.sDM(row[2]),
           'sDME': T.sDM(row[3]),
           'sDMA': T.sDM(row[4])
           }
      aSumme = aSumme + row[1]
      aAnzMonate = aAnzMonate + 1
      # print k
      ea.append(k)
    if aAnzMonate > 0:
      aSumme = aSumme / aAnzMonate
    return aAnzMonate, aSumme, ea

  def diagrammKostenartVonBis(self, aPfad, aDateiname, aData, aLabels):
    d = Drawing(800, 800)
    pie = Pie()
    pie.x = 360
    pie.y = 360
    pie.xradius = 300
    pie.yradius = 300
    pie.data = aData
    pie.labels = aLabels
    pie.slices.strokeWidth = 0.5
    # pie.slices[3].popout = 20
    d.add(pie)
    d.save(formats=['png'], outDir=aPfad, fnRoot=aDateiname)

  def diagrammAlleJahreEA(self, aPngDateiname):
    # Festlegen der Gesamtgröße in Pixel
    d = Drawing(800, 600)
    # Anlegen des Diagramms
    diagramm = VerticalBarChart()
    # Positionierung und Größe des Diagramms
    diagramm.x = 50
    diagramm.y = 50
    diagramm.width = 700
    diagramm.height = 500
    # Holen der Daten
    daten = []
    jahre = []
    aAnzJahre, aSumme, ea = self.listeAlleJahreEA()
    print(ea)
    for x in ea:
      print
      x['betrag'], x['jahr']
      daten.append(float(x['betrag']))
      jahre.append(str(x['jahr']))
    ymin = min(daten)
    ymax = max(daten)
    # Daten für das Diagramm müssen als Liste von Tupeln vorliegen
    daten = [tuple(daten)]
    print(daten)
    print(jahre)
    # return False
    # Hinzufügen der Daten
    diagramm.data = daten
    # Y-Achse (in ReportLab „valueAxis“) formatieren
    diagramm.valueAxis.valueMin = ymin
    diagramm.valueAxis.valueMax = ymax
    diagramm.valueAxis.valueStep = 2000
    # X-Achse (in ReportLab „categoryAxis“) formatieren
    diagramm.categoryAxis.categoryNames = jahre
    # Diagramm zeichnen
    d.add(diagramm)
    # ... und speichernhttp://www.reportlab.com/software/opensource/rl-toolkit/guide/
    print(aPngDateiname)
    renderPM.drawToFile(d, aPngDateiname, 'PNG')

  def jsonAlleJahreEA(self):
    aSumme, ea = self.listeAlleJahreEA()
    j = {'summe': T.sDM(aSumme), 'ea': ea}
    return j

  def htmlAlleJahreEA(self):
    aAnzahl, aSumme, ea = self.listeAlleJahreEA()
    s = ''
    for l in ea:
      jahr = l['jahr']
      # print type(konto),konto
      betrag = l['betrag']
      sSaldo = l['sDM']
      sDME = l['sDME']
      sDMA = l['sDMA']
      if (betrag < 0):
        aKlasse = 'class=table-right-currency-red'
      else:
        aKlasse = 'class=table-right-currency'
      # print type(konto),konto
      s = '%s <tr><td class=table-left>%s</td><td class=table-right-currency>%s</td><td class=table-right-currency>%s</td><td %s>%s</td></tr>' % (
        s, jahr, sDME, sDMA, aKlasse, sSaldo)
    return ("<table>"
            "<tr><th class=table-left>Jahr</th><th class=table-right-currency>Einnahmen</th><th class=table-right-currency>Ausgaben</th><th class=table-right-currency>Saldo</th></tr>"
            "%s"
            "<tr><th class=table-left>Durchschnitt für %d Jahre</th><th class=table-right-currency></th><th class=table-right-currency></th><th class=table-right-currency>%s</th></tr>"
            "</table>") % (s, aAnzahl, T.sDM(aSumme))
    return ("<table>"
            "<tr><th class=table-left>Jahr</th><th class=table-right-currency>Saldo</th></tr>"
            "%s"
            "<tr><th class=table-left>Durchschnitt</th><th class=table-right-currency>%s</th></tr>"
            "</table>") % (s, T.sDM(aSumme))

  def htmlAlleMonateEA(self):
    aAnzahl, aSumme, ea = self.listeAlleMonateEA()
    s = ''
    for l in ea:
      monat = "%2d/%d" % (l['monat'], l['jahr'])
      betrag = l['betrag']
      sSaldo = l['sDM']
      sDME = l['sDME']
      sDMA = l['sDMA']
      if (betrag < 0):
        aKlasse = 'class=table-right-currency-red'
      else:
        aKlasse = 'class=table-right-currency'
      # print type(konto),konto
      s = '%s <tr><td class=table-left>%s</td><td class=table-right-currency>%s</td><td class=table-right-currency>%s</td><td %s>%s</td></tr>' % (
        s, monat, sDME, sDMA, aKlasse, sSaldo)
    return ("<table>"
            "<tr><th class=table-left>Monat</th><th class=table-right-currency>Einnahmen</th><th class=table-right-currency>Ausgaben</th><th class=table-right-currency>Saldo</th></tr>"
            "%s"
            "<tr><th class=table-left>Durchschnitt für %d Monate</th><th class=table-right-currency></th><th class=table-right-currency></th><th class=table-right-currency>%s</th></tr>"
            "</table>") % (s, aAnzahl, T.sDM(aSumme))

  def getProjekt_ID(self, aKurz):
    aSQL = "SELECT MAX(ID) FROM KO_KUBPROJEKT P WHERE P.KURZ='%s'"
    aSQL = aSQL % (aKurz)
    print(aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return 0
    else:
      for row in cur:
        if (row[0]):
          return row[0]
        else:
          return 0

  def getProjekt_ID_Wintergarten_2017(self):
    return self.getProjekt_ID('Wintergarten 2017')

  def htmlProjekt(self, aProjekt_ID):
    aSumme, ea = self.listeProjekt(aProjekt_ID)
    s = ''
    for l in ea:
      datum = l['ttmmjj']  # .encode('utf-8')
      kurz = l['kurz']  # .encode('utf-8')
      betrag = l['betrag']
      s = '%s <tr><td class=table-3c-spalte1>%s</td><td class=table-3c-spalte2>%s</td><td class=table-3c-spalte3>%s</td></tr>' % (
        s, datum, kurz, betrag)
    return ("<table>"
            "<tr><th class=table-3c-spalte1>Datum</th><th class=table-3c-spalte2>Bezeichnung</th><th class=table-3c-spalte3>Betrag</th></tr>"
            "%s"
            "<tr><th class=table-3c-spalte1></th><th class=table-3c-spalte2>Summe</th><th class=table-3c-spalte3>%s</th></tr>"
            "</table>") % (s, T.sDM(aSumme))

  def htmlProjektK(self, aProjekt_ID):
    aSumme, ea = self.listeProjektK(aProjekt_ID)
    s = ''
    for l in ea:
      datum = l['ttmmjj']  # .encode('utf-8')
      kurz = l['kurz']  # .encode('utf-8')
      betrag = l['betrag']
      s = '%s <tr><td class=table-3c-spalte1>%s</td><td class=table-3c-spalte2>%s</td><td class=table-3c-spalte3>%s</td></tr>' % (
        s, datum, kurz, betrag)
    return ("<table>"
            "<tr><th class=table-3c-spalte1>Datum</th><th class=table-3c-spalte2>Bezeichnung</th><th class=table-3c-spalte3>Betrag</th></tr>"
            "%s"
            "<tr><th class=table-3c-spalte1></th><th class=table-3c-spalte2>Summe</th><th class=table-3c-spalte3>%s</th></tr>"
            "</table>") % (s, T.sDM(aSumme))

  def htmlProjektWintergarten2017(self):
    aProjekt_ID = self.getProjekt_ID_Wintergarten_2017()
    return self.htmlProjekt(aProjekt_ID)

  def htmlProjektWintergarten2017K(self):
    aProjekt_ID = self.getProjekt_ID_Wintergarten_2017()
    return self.htmlProjektK(aProjekt_ID)


def main():
  k = dmKonten()
  # print k.summeAlleKonten()
  # print k.listeAlleKonten()
  # print k.listeAlleJahreEA()
  # print k.listeProjektK(1)
  # print k.jsonAlleKonten()
  # print k.jsonLetzteEA()
  # print k.jsonAlleJahreEA()
  # print(k.htmlProjektWintergarten2017())
  print(k.htmldiagrammLetzterMonat())
  # k.analyseAusgabenVonBis(
  #  T.wnfDateToSQL(T.wnfErsterTagVormonat()),
  #  T.wnfDateToSQL(T.wnfLetzterTagVormonat()))
  # k.diagrammKostenartVonBis('/wnfdaten/wnfpython/wnfportal/trunk/src/wnfportal/m/diagramme/', 'kreis_2018_09',
  #                          '01.09.2018', '30.09.2018')
  # k.diagrammAlleJahreEA('/wnfdaten/wnfpython/wnfportal/trunk/src/wnfportal/m/diagramme/diagramm_alle_jahre.png')
  return 0


if __name__ == '__main__':
  main()
