from database import db
from message import send_message


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    zip_code = db.Column(db.Integer)
    phone_number = db.Column(db.String, unique=True)
    name = db.Column(db.String)

    def __init__(self, zip_code, phone_number, name):
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.name = name

    def __repr__(self):
        return '<User %d>' % self.id

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            send_message(self.phone_number, "Hello my name is PAL")
            return True
        except Exception:
            return False
