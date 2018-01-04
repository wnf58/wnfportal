#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import fdb
import os
import configparser
import wnfportal_dm_datenbank
import wnfportal_tools as T
import glob
import tempfile
import zipfile
import shutil
from xml.etree import cElementTree as ElementTree


class dmImportUmsaetze(wnfportal_dm_datenbank.dmDatenbank):
  def __init__(self):
    wnfportal_dm_datenbank.dmDatenbank.__init__(self)
    self.setIniDatei('wnfKuB.ini')
    self.importpfad = ''
    self.joker = ''

  def summeAlleKonten(self):
    aSQL = """
          SELECT SUM(BETRAG) FROM KO_KUBEA
          """
    return self.sqlSumme(aSQL)

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

  def letzteDatei(self):
    ini = configparser.ConfigParser()
    ini.read(self.IniDateiname)
    self.importpfad = T.leseIniStr(ini, T.SECTION_CAMT, "Downloads")
    self.joker = T.leseIniStr(ini, T.SECTION_CAMT, "Joker")
    # print importpfad,joker
    d = glob.glob(self.joker)
    if (len(d) == 0):
      return ''
    else:
      d.sort(reverse=True)
      # print(d)
      return d[0]

  def dateiEntpacken(self, aZipDateiname, aZielPfad):
    zip_ref = zipfile.ZipFile(aZipDateiname, 'r')
    zip_ref.extractall(path=aZielPfad)
    zip_ref.close()

  def auswertenXML(self, aXMLDatei):
    # http://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python
    print(aXMLDatei)

  def auswertenCAMT(self):
    dn = self.letzteDatei()
    if not T.wnfFileExists(dn):
      return -1
    # zp = tempfile.mkdtemp()
    zp = T.wnfTempDir()
    if (zp == ''):
      return -2
    # print zp
    self.dateiEntpacken(dn, zp)
    d = glob.glob('%s/*.xml' % (zp))
    d.sort()
    # print d
    for xml in d:
      self.auswertenXML(xml)
    # shutil.rmtree(zp)
    return 0


def main():
  k = dmImportUmsaetze()
  print(k.letzteDatei())
  anz = k.auswertenCAMT()
  if anz == -1:
    print('Es wurde keine Datei %s zur Auswertung gefunden' % (k.joker))
  elif anz == 0:
    print('Es gab in der Datei keine neuen Umsätze')
  else:
    print("%d Umsätze ausgewertet." % (anz))
  return anz


if __name__ == '__main__':
  main()
