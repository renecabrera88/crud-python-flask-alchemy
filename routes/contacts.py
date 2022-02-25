# en este achivo van a estar todas las rutas
#usando blueprint.
#render_template se usa para renderizar los archivos
#from crypt import methods, este aparecio
#request es una funcion que m,e permite leer los datos que vienen del form y recibirlos en el backend  
#redirect es una funcion que permite redireccionar a otra pagina despues, por ejemplo, de guardar un usuario 
#igual que en los template, sirve para redireccionar a una funcion y no a un endpoint
#from crypt import methods
#flah, esta funcion permite mandar mensaje de exto.
from flask import Blueprint, render_template, request, redirect, url_for, flash
#importamos la clase contact para intanciar los datos y guardarlos
from models.contact import Contact
#exportamos la conecacion de la base de datos para poder guardar y/o modificar en la base de datos
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route("/")
def home():
    #Contact.query.all() es el equivalente a "select * from contact" 
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@contacts.route('/new', methods=['POST'])
def add_contact():
    #extraemos los datos del formulario que esta en el request
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    #instancio un objeto y paso los parametros a la clase por la funcion contructor __init__
    #que solicita esos 3 parametros (revisar model/contact.py/ def __init__)
    new_contact = Contact(fullname, email, phone)
    #a continuacion guardamos el objeto en la base de datos, es similar a los comandos de git
    #el primero agrega a un stage y el segundo guarda con un commit
    db.session.add(new_contact)
    db.session.commit()

    #mensaje que todo salio bien
    flash('Contact added successfully')
    #finalmente redirijer a la direccion raiz
    return redirect('/')

#en este caso, por usar la funcion url_for, puedo acceder directamente a la funcionupdate
# por lo que no es necesario colocar el id que se recibe en la url como '/update/<id>'
@contacts.route('/update/<id>', methods = ['POST', 'GET'])
def update(id):
    #consulto por la data por el id,
    #Contact.query.get(id) es equivalente a select * from contact where id='id'
    contact = Contact.query.get(id)
    #si el meto es post, entonces actualizo, sino paso a renderizar template    
    if request.method =='POST':
        #asigno los valores del formulario a los valores de contact
        contact.fullname = request.form['fullname']
        contact.phone = request.form['phone']
        contact.email = request.form['email']
        #guardo contatc en la base de datos.
        db.session.commit()
        flash('Contact added successfully')
        return redirect(url_for('contacts.home'))

    #renderizo template update.html y le envio la informacion obtenida en el query anterior
    return render_template('update.html', contact= contact)

@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact added successfully')
    #me redicciona en vez al endpoint a la funcion de ese endpoint, gracias a la funcion de flask url_for
    return redirect(url_for('contacts.home'))

@contacts.route('/about')
def about():
    return render_template('about.html')