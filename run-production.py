from MemberRegister import db

from MemberRegister.model import *

db.create_all()

if __name__ == '__main__':
    from MemberRegister import app
    from gevent.pywsgi import WSGIServer

    WSGIServer(("0.0.0.0", 8080), app).serve_forever()
