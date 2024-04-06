from . import db
from flask_login import UserMixin

# # Define associations between tables
# comenzi_reciclare = db.Table(
#     'comenzi_reciclare',
#     db.Column('tip_deseu_id', db.Integer, db.ForeignKey('tip_deseu.id'), primary_key=True),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
# )

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    tip_user = db.Column(db.String(30), nullable=False)
    
    # # Establish relationship with Tip_Deseu
    # tip_deseuri = db.relationship('Tip_Deseu', secondary=comenzi_reciclare, backref='users')

    # # Establish relationship with Note
    # notes = db.relationship('Note', backref='user', lazy=True)

class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# class Locatie(db.Model):
#     __tablename__ = 'locatie'

#     id = db.Column(db.Integer, primary_key=True)
#     localitate = db.Column(db.String(30), nullable=False)
#     strada = db.Column(db.String(30), nullable=False)
#     bloc = db.Column(db.String(2), nullable=False)

# class Tip_Deseu(db.Model):
#     __tablename__ = 'tip_deseu'

#     id = db.Column(db.Integer, primary_key=True)
#     cantitate = db.Column(db.Integer, nullable=False)
