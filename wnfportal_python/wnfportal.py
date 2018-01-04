#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

#  wnfportal.py
#
#  Copyright 2014 Uwe Wilske KiDO <wnf@c2012>
#
#

import os
import cherrypy
import socket
import time
import json
import datetime
from datetime import timedelta
import locale
from wnfportal_dm import object_q

ENTWICKLUNG = True


# Dict zur Steuerung des Servers
def server_dict():
  '''Erstellung der Konfiguration für CherryPy'''
  g = {}
  g['tools.staticdir.root'] = os.path.dirname(os.path.abspath(__file__))
  g['server.socket_port'] = 8080
  g['server.socket_host'] = '0.0.0.0'
  g['tools.sessions.on'] = True
  g['tools.sessions.timeout'] = 1000
  g['tools.sessions.name'] = "wnfportalid"
  if ENTWICKLUNG:
    g['tools.sessions.storage_type'] = "File"
    g['tools.sessions.storage_path'] = '/tmp/'
  else:
    g['environment'] = "production"
  c = {'global': g}
  # c['/']={'tools.staticdir.on':True,'tools.staticdir.dir':"www",'tools.staticdir.index' : "index.html"}
  c['/'] = {'tools.staticdir.on': True, 'tools.staticdir.dir': "m", 'tools.staticdir.index': "index.html"}
  return c


class wnfPortal(object):
  def __init__(self):
    self.q = object_q()
    print(dir(self.q))

  def index(self):
    return "Die Datei index.html fehlt."

  index.exposed = True


def main():
  cherrypy.quickstart(wnfPortal(), config=server_dict())
  return 0


if __name__ == '__main__':
  main()
