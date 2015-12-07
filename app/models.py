from app import db,app

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    zip_code = db.Column(db.Integer)
    phone_number = db.Column(db.String,unique=True)

    def __init__(self,zip_code,phone_number):
    	self.zip_code = zip_code
    	self.phone_number = phone_number