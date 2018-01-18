#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

#  wnfportal_tools.py

import configparser
import locale
from datetime import date, timedelta
import os

SECTION_SETUP = 'Setup'
SECTION_CAMT = 'CAMT'
TEMPPFAD = '/tmp/wnfportal'


def leseIniStr(ini, aSection, aName):
  try:
    s = ini.get(aSection, aName)
  except configparser.NoOptionError:
    s = ""
  return s


def wnfHeute():
  return date.today()


def wnfErsterDieserMonat():
  heute = wnfHeute()
  return date(heute.year, heute.month, 1)


def wnfLetzterTagVormonat():
  return wnfErsterDieserMonat() - timedelta(1)


def wnfErsterTagVormonat():
  d = wnfLetzterTagVormonat()
  return date(d.year, d.month, 1)


def sDM(aBetrag):
  locale.setlocale(locale.LC_ALL, 'de_DE.UTF-8')
  if not aBetrag:
    aBetrag=0
  return locale.currency(aBetrag, grouping=True)
  # return '{:20,.2f}'.format( aBetrag )


def wnfDateToSQL(aDatum):
  return ("'%d/%d/%d'") % (aDatum.year, aDatum.month, aDatum.day)


def wnfSQLSumme(aCon, aSQL):
  cur = aCon.cursor()
  cur.execute(aSQL)
  for row in cur:
    return row[0]
  return 0


def wnfSQLCount(aCon, aSQL):
  cur = aCon.cursor()
  cur.execute(aSQL)
  for row in cur:
    return row[0]
  return 0


def wnfFileExists(aDateiname):
  b = os.path.exists(aDateiname)
  if (b):
    b = os.path.isfile(aDateiname)
  return b


def wnfForceDir(aPfad):
  # print(aPfad)
  if not os.path.exists(aPfad):
    os.makedirs(aPfad)
  return os.path.exists(aPfad)


def wnfTempDir():
  if (wnfForceDir(TEMPPFAD)):
    return TEMPPFAD
  else:
    return ''


def main():
  print(sDM(9999.77))
  print(wnfDateToSQL(wnfErsterTagVormonat()))
  print(wnfTempDir())
  return 0


if __name__ == '__main__':
  main()
