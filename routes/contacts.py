# en este achivo van a estar todas las rutas
#usando blueprint
from flask import Blueprint, render_template

contacts = Blueprint('contacts', __name__)

@contacts.route("/")
def home():
    return render_template('index.html')

@contacts.route('/new')
def add_contact():
    return "Saving a Contact"

@contacts.route('/update')
def update():
    return "Update a Contact"

@contacts.route('/delete')
def delete():
    return "Delete a Contact"

@contacts.route('/about')
def about():
    return render_template('contact.html')