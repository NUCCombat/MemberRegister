from .. import db


class Member(db.Model):
    __tablename__ = 'member'
    uid = db.Column(db.Integer, autoincrement=True, default=1, nullable=False)
    member_id = db.Column(db.String(10), primary_key=True, nullable=False)
    member_sex = db.Column(db.String(2), nullable=False)
    member_name = db.Column(db.String(8), nullable=False)
    member_college = db.Column(db.String(20), nullable=False)
    member_WeChat = db.Column(db.String(64), unique=True)
    member_QQ = db.Column(db.String(12), unique=True)
    member_telephone = db.Column(db.String(20), nullable=False)
    member_political_status = db.Column(db.String(10), nullable=False)
    member_email = db.Column(db.String(64))
    member_birthday = db.Column(db.String(64), nullable=False)

    def __init__(self, member_name, member_id, member_sex, member_college, member_wechat,
                 member_qq, member_telephone, member_political_status, member_email,
                 member_birthday):
        self.member_name = member_name
        self.member_id = member_id
        self.member_sex = member_sex
        self.member_college = member_college
        self.member_WeChat = member_wechat
        self.member_QQ = member_qq
        self.member_telephone = member_telephone
        self.member_political_status = member_political_status
        self.member_email = member_email
        self.member_birthday = member_birthday

    def __repr__(self):
        return "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (self.member_name, self.member_id,
                                                            self.member_sex, self.member_college,
                                                            self.member_WeChat, self.member_QQ,
                                                            self.member_political_status, self.member_email,
                                                            self.member_email, self.member_birthday)
