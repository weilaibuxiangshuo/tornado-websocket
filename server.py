import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import options
from application import Application
import config


if __name__=="__main__":
    options.parse_command_line()
    app=Application()
    httpserver=tornado.httpserver.HTTPServer(app)
    httpserver.bind(config.options['port'])
    httpserver.start()
    tornado.ioloop.IOLoop.current().start()