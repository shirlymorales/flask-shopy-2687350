from flask import render_template, redirect, flash
from . import clientes
import app
from .forms import NewClientForm, EditClientForm
import os 

#rutas del modulo "clientes"
@clientes.route("/listar")
def listar():
    # Listar los clientes utilizando modelos
    clientes = app.models.Cliente.query.all()
    return render_template("index_cliente.html", 
                           clientes = clientes)
    
@clientes.route("/nuevo", 
                 methods =["GET", "POST"])
def nuevo():
    #definir el formulario
    form = NewClientForm()
    #definir el objeto producto vacio
    c = app.models.Cliente()
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.add(c)
        app.db.session.commit()
        ##return os.getcwd()
        #extraer el objeto FileStorage
        flash("Cliente registrado correctamente")
        return redirect("/clientes/listar")
    
    return render_template("new.html",
                           operacion = "Nuevo", 
                           form = form)
@clientes.route("/editar/<cliente_id>",
                 methods= ['GET', 'POST'])
def editar(cliente_id):
    c = app.models.Cliente.query.get(cliente_id)
    form = EditClientForm(obj = c)
    if form.validate_on_submit():
        form.populate_obj(c)
        app.db.session.commit()
        flash("Cliente actualizado correctamente")
        return redirect("/clientes/listar")
    
    return render_template("new.html",
                           operacion = "Actualizar",
                           form = form)

@clientes.route('/eliminar/<cliente_id>')
def eliminar(cliente_id):
    c = app.models.Cliente.query.get(cliente_id)
    app.db.session.delete(c)
    app.db.session.commit()
    flash("Cliente Eliminado")  
    return redirect("/clientes/listar") 
    
    
    