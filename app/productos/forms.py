from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField ,SubmitField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired,FileAllowed

class RegistrarProductoForm(FlaskForm):
    nombre = StringField("nombre del producto: " ,validators = [InputRequired(message="Mama huevo! Nombre del producto requerido")])
    precio = IntegerField("precio del producto: " , validators = [InputRequired(message="Mama huevo! Precio Requerido"),
                                                                  NumberRange(message="Mama huevo! Precio fuera de rango", 
                                                                              min =10, 
                                                                              max =100000)
                                                                  ])
    imagen = FileField("Seleccione imagen del producto:",
                       validators = [FileRequired(message = "debe seleccionar una imagen"),
                                     FileAllowed(['jpg' , 'png'], 
                                                 "solo se permite imagenes") 
                                     ])
    Submit = SubmitField("Guardar")