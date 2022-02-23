# este archivo tiene la configuracion de la aplicacion
from flask import Flask
#from sqlalchemy import false
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy


#aqui se configuras la coneccion a la BD ya que no se puede en 
#db.py por necesitar a app en su configuracion, y finalmente de 
# envia app a SQLAlquemy. Los modelos de las tablas, que serán 
#las clases se coloca en models
app = Flask(__name__)

app.secret_key = 'secret key'

app.config["SQLALCHEMY_DATABASE_URI"] ='mysql://rene:1234@localhost/contactsdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

app.register_blueprint(contacts)
