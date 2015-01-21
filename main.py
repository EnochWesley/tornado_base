import tornado.ioloop
import website.app

website.app.application.listen(8888)
tornado.ioloop.IOLoop.instance().start()
