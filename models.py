from ext import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(),nullable=False)