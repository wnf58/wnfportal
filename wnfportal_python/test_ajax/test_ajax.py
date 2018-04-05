# https://www.tutorialspoint.com/cherrypy/cherrypy_use_of_ajax.htm
import cherrypy
import webbrowser
import os
import json


MEDIA_DIR = os.path.join(os.path.abspath("."), u"media")


class AjaxApp(object):
  @cherrypy.expose
  def index(self):
    return open(os.path.join(MEDIA_DIR, u'index.html'))

  @cherrypy.expose
  def submit(self, name):
    print(name)
    cherrypy.response.headers['Content-Type'] = 'application/json'
    k = {'title': "Hello, %s" % name}
    print(k)
    j = json.dumps(k)
    # aus dem String j müssen Bytes gemacht werden, damit diese als JSON-Object an die HTML-Datei übergeben werden
    j = j.encode()
    print(j)
    return j



config = {'/media':
            {'tools.staticdir.on': True,
             'tools.staticdir.dir': MEDIA_DIR, }
          }


def open_page():
  webbrowser.open("http://127.0.0.1:8080/")


cherrypy.engine.subscribe('start', open_page)
cherrypy.tree.mount(AjaxApp(), '/', config=config)
cherrypy.engine.start()
