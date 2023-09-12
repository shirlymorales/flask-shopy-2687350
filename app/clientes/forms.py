from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField ,validators ,SubmitField, PasswordField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired,FileAllowed


class ClienteForm():
    username = StringField("usuario: " ,validators = [InputRequired(message="Mama huevo! Usuario requerido")])
    password = PasswordField ("contraseña: ", [validators.Length(min=10 , max=16)])
    email = StringField("correo: " , [validators.Length(min=6 , max=35)])
    
    
class NewClientForm(FlaskForm, ClienteForm):    

    Submit = SubmitField("Guardar")

class EditClientForm(FlaskForm, ClienteForm):
    submit = SubmitField("Actualizar")    