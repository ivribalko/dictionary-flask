from main import db

class Vocabulary(db.Model):
    __tablename__ = 'vocabulary'
    word = db.Column(db.String(), primary_key=True)
    synonym = db.Column(db.String())

