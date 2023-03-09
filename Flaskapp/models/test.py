from Flaskapp.extensions import db

class Test(db.Model):
    id     = db.Column(db.Integer , primary_key = True)
    fname  = db.Column(db.String(50))
    lname  = db.Column(db.String(50))