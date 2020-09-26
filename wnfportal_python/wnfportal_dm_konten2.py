import wnfportal_dm_datenbank
import wnfportal_tools as T


class dmKonten(wnfportal_dm_datenbank.dmDatenbank):
  def __init__(self):
    wnfportal_dm_datenbank.dmDatenbank.__init__(self)
    self.setIniDatei('wnfKuB.ini')
    # self.setIniDatei('wnfKITAOffice.ini')

  def dreiSpaltig(self, aSQL, c1, c2, c3, aLink, c4):
    rows = self.listTabelleAsRows(aSQL)
    css = []
    aSumme = 0
    aAnz = 0
    s = '<th class=table-3c-spalte1>%s</th><th class=table-3c-spalte2>%s</th><th class=table-3c-spalte3>%s</th>'
    s = s % ('Datum', 'Bezeichnung', 'Betrag')
    css = css + [s]
    for r in rows:
      s = '<td class=table-3c-spalte1>%s</td><td class=table-3c-spalte2>%s</td><td class=table-3c-spalte3>%s</td>'
      if c4 and r[c4]:
        aHref = '<a href="%s/%d">%s</a>' % (aLink, r[c4], r[c2])
      else:
        aHref = r[c2]
      s = s % (r[c1], aHref, T.sDM(r[c3]))
      css = css + [s]
      aSumme = aSumme + r[c3]
      aAnz += 1
    s = '<td class=table-3c-spalte1>%s</td><td class=table-3c-spalte2>%s</td><td class=table-3c-spalte3>%s</td>'
    s = s % (aAnz, '', T.sDM(aSumme))
    css = css + [s]
    return css

  def rowsLetzteEA(self):
    aSQL = """
              SELECT E.ID,E.DATUM,E.KURZ,E.BETRAG,E.KAT_ID
              FROM KO_KUBEA E
              WHERE E.DATUM >= %s
              ORDER BY E.DATUM DESC,E.KURZ
            """
    aSQL = aSQL % (T.wnfDateToSQL(T.wnfTagVorVor8Wochen()))
    print(aSQL)
    return self.dreiSpaltig(aSQL, 1, 2, 3, '/kategorie_ea', 4)

  def rowsKategorieEA(self, aKat_ID):
    aSQL = """
              SELECT E.ID,E.DATUM,E.KURZ,E.BETRAG,E.KST_ID
              FROM KO_KUBEA E
              WHERE E.KAT_ID = %s
              ORDER BY E.DATUM DESC,E.KURZ
            """
    aSQL = aSQL % aKat_ID
    print(aSQL)
    return self.dreiSpaltig(aSQL, 1, 2, 3, '/kostenstelle_ea', 4)

  def rowsKostenstelleEA(self, aKst_ID):
    aSQL = """
              SELECT E.ID,E.DATUM,E.KURZ,E.BETRAG,E.KAT_ID
              FROM KO_KUBEA E
              WHERE E.KST_ID = %s
              ORDER BY E.DATUM DESC,E.KURZ
            """
    aSQL = aSQL % aKst_ID
    print(aSQL)
    return self.dreiSpaltig(aSQL, 1, 2, 3, '/kategorie_ea', 4)
