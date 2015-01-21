import os.path

settings = {
    'debug':True,
    'static_path':os.path.join(os.path.dirname(__file__), 'staticfiles'),
    'template_path':os.path.join(os.path.dirname(__file__), 'templates')
}

platform = 'tornado.platform.asyncio.AsyncIOLoop'
