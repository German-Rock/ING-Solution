from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . models import Comenzi_reciclare
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        recycle = request.form.get('type_of_recycle')
        quantity = request.form.get('quantity_int_tone')

        if len(recycle) < 1:
            flash('Type of recycle is too short!', category='error') 
        else:
            new_comanda = Comenzi_reciclare(type_of_recycle=recycle, quantity_int_tone=quantity, user_id=current_user.id)
            db.session.add(new_comanda)
            db.session.commit()
            flash('Comanda a fost adaugata!', category='success')

    return render_template("home.html", user_comm_table=Comenzi_reciclare.query.filter_by(user_id=current_user.id), user=current_user)


# @views.route('/delete-note', methods=['POST'])
# def delete_note():  
#     note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})


@views.route('/ceva', methods=['GET', 'POST'])
def ceva():
    if request.method == 'POST': 
        message = request.form.get('message')#Gets the note from the HTML
        name = request.form.get('name')
        email = request.form.get('email')
        print(message,name,email)

    return render_template('buttnresponse.html')

