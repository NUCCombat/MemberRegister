from .. import db


class Paid(db.Model):
    student_id = db.Column(db.String(10), primary_key=True, nullable=False)

    def __init__(self, student_id):
        self.student_id = student_id

