#Este archivo arranca la aplicacion y
#trae la configuracion de la aplicacion app.py
from app import app
from utils.db import db

#cuando arranque la aplicacion crea las tablas definidas en
#model/contact.py
with app.app_context():
    db.create_all()
 
if __name__ == "__main__":
    #debug=true es el equivalente a nodemon, cuando guardo reinicia programa
    app.run(debug=True)