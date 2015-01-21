from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from . import urls
from . import config

application = Application(urls.urlpattern, **config.settings)
if config.platform:
    IOLoop.configure(config.platform)


