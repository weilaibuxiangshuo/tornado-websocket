from tornado.web import Application,url
from views import view
import config

class Application(Application):
    def __init__(self):
        handler = [
            (r'/', view.Indexhandler),
            url(r'/home', view.Homehandler,name="home"),
            url(r'/students', view.Studentshandler,name="students"),
            url(r'/students2', view.Students2handler,name="students2"),
            url(r'/world', view.Worldhandler,name="world"),
            url(r'/chat', view.Chathandler,name="chat")
        ]
        super(Application, self).__init__(handler,**config.settings)
