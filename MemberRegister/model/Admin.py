from .. import db


class Admin(db.Model):
    __tablename__ = 'admin'
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password
