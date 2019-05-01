#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

#  wnfportal_dm_datenbank.py
#
#  Copyright 2014 Uwe Wilske <wnf@c2012>
#

import os
import fdb
import configparser
import wnfportal_tools as T


class dmDatenbank(object):
  def __init__(self):
    self.Con = None
    self.ibconf_server = "localhost"
    self.ibconf_user = "SYSDBA"
    self.ibconf_database = ""
    self.ibconf_password = "masterkey"
    self.IniDateiname = ''
    self.Verbunden = False

  def setIniDatei(self, aIniDatei):
    self.IniDateiname = os.environ["HOME"]
    self.IniDateiname = "%s/.config/wlsoft/%s" % (self.IniDateiname, aIniDatei)
    print(self.IniDateiname)

  def isVerbunden(self):
    if (self.Verbunden):
      return True
    if os.path.exists(self.IniDateiname):
      ini = configparser.ConfigParser()
      ini.read(self.IniDateiname)
      self.ibconf_server = T.leseIniStr(ini, T.SECTION_SETUP, "SERVER")
      self.ibconf_user = T.leseIniStr(ini, T.SECTION_SETUP, "USER_NAME")
      self.ibconf_database = T.leseIniStr(ini, T.SECTION_SETUP, "DATABASE")
      self.ibconf_password = T.leseIniStr(ini, T.SECTION_SETUP, "PASSWORD")
      self.Con = fdb.connect(
        host=self.ibconf_server,
        database=self.ibconf_database,
        user=self.ibconf_user,
        password=self.ibconf_password,
        charset='UTF8')
      self.Verbunden = True
      return True
    else:
      print("Inidatei %s fehlt." % (self.IniDateiname))
      self.Verbunden = False
      return False

  def sqlCount(self, aSQL):
    if not self.isVerbunden():
      return 0
    return T.wnfSQLCount(self.Con, aSQL)

  def sqlSumme(self, aSQL):
    if not self.isVerbunden():
      return 0.00
    return T.wnfSQLSumme(self.Con, aSQL)

  def sqlOpen(self, aSQL):
    if not self.isVerbunden():
      return None
    cur = self.Con.cursor()
    cur.execute(aSQL)
    return cur

  def closeConnection(self):
    self.Con.close()
    self.Verbunden = False


def main():
  d = dmDatenbank()
  d.setIniDatei('wnfKontakt.ini')
  if (d.isVerbunden()):
    aSQL = """
          SELECT COUNT(*) FROM KO_TERMIN T 
          """
    print(d.sqlCount(aSQL))
  return 0


if __name__ == '__main__':
  main()
