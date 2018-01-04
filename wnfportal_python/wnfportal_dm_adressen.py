#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import fdb
import os
import configparser
import wnfportal_dm_datenbank
import wnfportal_tools as T


class dmAdressen(wnfportal_dm_datenbank.dmDatenbank):
  def __init__(self):
    wnfportal_dm_datenbank.dmDatenbank.__init__(self)
    self.setIniDatei('wnfKontakt.ini')

  def anzahlAlleAufgaben(self):
    aSQL = """
          SELECT COUNT(*) FROM KO_TODO T
          WHERE T.ERLEDIGT='N'
          """
    return self.sqlCount(aSQL)

  def listeAlleAufgaben(self):
    aSQL = """
            SELECT T.ID,T.KURZ,T.LANG,T.PRIO FROM KO_TODO T
            WHERE T.ERLEDIGT='N'
            ORDER BY T.PRIO DESC,T.KURZ
          """
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return []
    aufgaben = []
    for row in cur:
      a = {'todo_id': row[0], 'aufgabe': row[1], 'prio': str(row[3])}
      print(a)
      aufgaben.append(a)
    return aufgaben

  def jsonAlleAufgaben(self):
    j = {'anzahl': str(self.anzahlAlleAufgaben()), 'aufgaben': self.listeAlleAufgaben()}
    return j

  def anzahlAlleAdressen(self, aWhere=''):
    aSQL = """
          SELECT COUNT(*) FROM KO_ADR A %s
          """
    aSQL = aSQL % (aWhere)
    return self.sqlCount(aSQL)

  def listeAlleAdressen(self, aWhere='', aOrderBy='ORDER BY A.KURZ'):
    aSQL = """
            SELECT A.ID,A.ART,A.KURZ,A.TEL1,A.HANDY,A.EMAIL FROM KO_ADR A
            %s
            %s
          """
    aSQL = aSQL % (aWhere, aOrderBy)
    # print (aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return []
    adressen = []
    for row in cur:
      a = {
        'adr_id': row[0],
        'art': row[1],
        'kurz': row[2],
        'tel': row[3],
        'handy': row[4],
        'email': row[5]}
      if (a['tel'] == None):
        a['tel'] = ''
      if (a['email'] == None):
        a['email'] = ''
      if (a['handy'] == None):
        a['handy'] = ''
      print(a)
      adressen.append(a)
    return adressen

  def jsonAlleAdressen(self):
    j = {'anzahl': str(self.anzahlAlleAdressen()), 'adressen': self.listeAlleAdressen()}
    return j

  def jsonTop10Adressen(self):
    aWhere = 'WHERE A.TOP10 <> 0'
    aOrderBy = 'ORDER BY A.TOP10 DESC, A.KURZ';
    j = {'anzahl': str(self.anzahlAlleAdressen(aWhere)),
         'adressen': self.listeAlleAdressen(aWhere, aOrderBy)}
    return j

  def eineAdresse(self, aID):
    aSQL = """
            SELECT A.ID,A.ART,A.KURZ,A.TEL1,A.HANDY,A.EMAIL FROM KO_ADR A
            WHERE A.ID = %s
          """
    aSQL = aSQL % (aID)
    # print (aSQL)
    cur = self.sqlOpen(aSQL)
    if (cur == None):
      return {}
    a = {}
    for row in cur:
      a = {
        'adr_id': row[0],
        'art': row[1],
        'kurz': row[2],
        'tel': row[3],
        'handy': row[4],
        'email': row[5]}
      if (a['tel'] == None):
        a['tel'] = ''
      if (a['email'] == None):
        a['email'] = ''
      if (a['handy'] == None):
        a['handy'] = ''
      print(a)
    return a

  def jsonEineAdresse(self, aID):
    j = self.eineAdresse(aID)
    return j


def main():
  a = dmAdressen()
  # print a.anzahlAlleAufgaben()
  # print a.listeAlleAufgaben()
  print(a.jsonAlleAufgaben())
  # print a.jsonAlleAdressen()
  print(a.jsonTop10Adressen())
  print(a.jsonEineAdresse(1226))
  return 0


if __name__ == '__main__':
  main()
