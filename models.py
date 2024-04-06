from .models import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Locatie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    localitate = db.Column(db.String(30))
    strada = db.Column(db.String(30))
    bloc = db.Column(db.String(2))
    
# Definirea tabelei de asociere (tabelul intermediar)
comenzi_reciclare = db.Table(
    'comenzi_reciclare',
    db.Column('tip_deseu_id', db.Integer, db.ForeignKey('tip_deseu.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class Tip_Deseu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantitate = db.Column(db.Integer)
    
class Comanda(db.Model): 
    data = db.Column(db.DateTime(timezone=True), default=func.now())
    
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    tip_user = db.Column(db.String(30))
    tip_deseuri = db.relationship('Tip_Deseu', secondary=comenzi_reciclare, backref=db.backref('users', lazy='dynamic'))
    

    
    
    
    