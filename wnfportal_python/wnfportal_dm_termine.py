#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

#  wnfportal_dm_termine.py
#
#  Copyright 2014 Uwe Wilske <wnf@c2012>
#


import wnfportal_dm_datenbank
import wnfportal_tools as T


class dmTermine(wnfportal_dm_datenbank.dmDatenbank):
  def __init__(self):
    wnfportal_dm_datenbank.dmDatenbank.__init__(self)
    self.setIniDatei('wnfKontakt.ini')

  def anzahlAlleTermine(self, aWhere=''):
    aSQL = """
          SELECT COUNT(*) FROM KO_TERMIN T %s
          """
    aSQL = aSQL % (aWhere)
    return self.sqlCount(aSQL)

  def listeAlleTermine(self, aWhere=''):
    if not self.Verbunden:
      self.verbinden()
    if not self.Verbunden:
      return []
    aSQL = """
            SELECT T.ID,T.KURZ,T.VON,T.BIS
            FROM KO_TERMIN T
            %s
            ORDER BY T.VON,T.KURZ
          """
    aSQL = aSQL % (aWhere)
    cur = self.Con.cursor()
    cur.execute(aSQL)
    termine = []
    for row in cur:
      k = {'termin_id': row[0], 'termin': row[1], 'von': str(row[2]), 'bis': str(row[3])}
      print(k)
      termine.append(k)
    return termine

  def jsonAlleTermine(self):
    aWhere = 'WHERE CURRENT_DATE <=T.VON'
    j = {'anzahl': str(self.anzahlAlleTermine(aWhere)), 'termine': self.listeAlleTermine(aWhere)}
    return j


def main():
  t = dmTermine()
  aWhere = 'WHERE CURRENT_DATE <=T.VON'
  print(t.anzahlAlleTermine(aWhere))
  t.listeAlleTermine(aWhere)
  return 0


if __name__ == '__main__':
  main()
