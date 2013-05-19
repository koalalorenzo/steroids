import os

__help__ = """
"""


requirements = [
    "tornado"
]

directories = [
    "[base]",
    ]

files = [
    "[base]/tornado.py",
    ]

def install(basepath, name):
    """
        Install Tornado Module
    """
    
    tornado_file = open(os.path.join(basepath,"tornado.py"), "w")
    tornado_file.write("from tornado.wsgi import WSGIContainer\n")
    tornado_file.write("from tornado.httpserver import HTTPServer\n")
    tornado_file.write("from tornado.ioloop import IOLoop\n")
    tornado_file.write("from configuration import SERVER_PORT\n")
    tornado_file.write("from %s import app as application\n" % name)
    tornado_file.write("\n")
    tornado_file.write("http_server = HTTPServer(WSGIContainer(application))\n")
    tornado_file.write("http_server.listen(SERVER_PORT)\n")
    tornado_file.write("IOLoop.instance().start()\n")
    tornado_file.close()
    return
    
def install_examples(basepath, name):
    """
        Install Tornado Module with example files
    """
    return