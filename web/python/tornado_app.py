#!/usr/bin/env python

import os
import platform
import tornado.ioloop
import tornado.options
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!<br/> I am " + platform.node() +
                   " listening on " + os.environ['TORNADO_PORT'])

def make_app():
    settings = {
        'debug': True
    }

    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(os.environ['TORNADO_PORT'])
    tornado.ioloop.IOLoop.current().start()