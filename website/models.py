from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import validates



class Comenzi_reciclare(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    _type_of_recycle = db.Column(db.String(100))
    quantity_int_tone = db.Column(db.Integer)   
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @property
    def type_of_recycle(self):
        return self._type_of_recycle

    @type_of_recycle.setter
    def type_of_recycle(self, value):
        valid_types = {"plastic", "hartie/carton", "sticla", "organic", "electronic"}
        if value.lower() not in valid_types:
            raise ValueError(f"Invalid type_of_recycle: {value}. Allowed values are: {', '.join(valid_types)}")
        self._type_of_recycle = value.lower()

    @validates('quantity_int_tone')
    def validate_quantity_int_tone(self, key, quantity_int_tone):
        if quantity_int_tone < 0:
            raise ValueError("Quantity (in tons) must be a positive number")
        return quantity_int_tone


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    user_type = db.Column(db.String(150))
    localitate = db.Column(db.String(30))
    strada = db.Column(db.String(30))
    bloc = db.Column(db.String(5))
    notes = db.relationship('Comenzi_reciclare')
    
    
# # Definirea tabelei de asociere (tabelul intermediar)
# comenzi_reciclare = db.Table(
#     'comenzi_reciclare',
#     db.Column('tip_deseu_id', db.Integer, db.ForeignKey('tip_deseu.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

class Tip_Deseu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantitate = db.Column(db.Integer)
    
# class Comanda(db.Model): 
#     data = db.Column(db.DateTime(timezone=True), default=func.now())
    
    
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30))
#     email = db.Column(db.String(150), unique=True)
#     password = db.Column(db.String(150))
#     tip_user = db.Column(db.String(30))
#     tip_deseuri = db.relationship('Tip_Deseu', secondary=comenzi_reciclare, backref=db.backref('users', lazy='dynamic'))