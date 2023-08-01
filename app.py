# dependencias del proyecto
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# crear el objeto de aplicación
app = Flask(__name__)
#configurar app para conectarse a bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask-shopy-2687350'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# crear el objeto sqlalchemy
db = SQLAlchemy(app)
#crear el objeto de migracion y activarlo
migrate = Migrate(app , db)

##Modelos <<entities>>
class Cliente(db.Model):
    
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    email = db.Column(db.String(120))





