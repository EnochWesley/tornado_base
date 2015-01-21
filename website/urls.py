from tornado.web import url
from .handlers import MainHandler

urlpattern = [
    url(r'/', MainHandler, {}, name='main'),
]

