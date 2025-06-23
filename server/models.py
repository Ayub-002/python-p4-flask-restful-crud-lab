from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import Numeric

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    name = db.Column(db.String ,nullable=False)
    image = db.Column(db.String, nullable=False)
    price= db.Column(Numeric(10,2), nullable=False)

    id = db.Column(db.Integer, primary_key=True)