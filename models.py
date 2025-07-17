from ext import db

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()


class Item(db.Model, BaseModel):
    __tablename__ = "items"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    image = db.Column(db.String(),nullable=False)


class User(db.Model, BaseModel):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(),nullable=False)
