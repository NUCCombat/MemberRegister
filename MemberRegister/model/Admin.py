from .. import db


class Admin(db.Model):
    __tablename__ = 'admin'
    username = db.Column(db.String(32), primary_key=True, nullable=False)
    password = db.Column(db.String(32), nullable=False)
