# este archivo tiene la configuracion de la aplicacion
from flask import Flask
#from sqlalchemy import false
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
#importo del archivo config la variable DATABASE_CONNECTION_URI que es un string de coneccion
from config import DATABASE_CONNECTION_URI

#aqui se configuras la coneccion a la BD ya que no se puede en 
#db.py por necesitar a app en su configuracion, y finalmente de 
# envia app a SQLAlquemy. Los modelos de las tablas, que serán 
#las clases se coloca en models
app = Flask(__name__)

app.secret_key = 'secret key'

#conecto la bd
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLAlchemy(app)

app.register_blueprint(contacts)
