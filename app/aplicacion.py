from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from model import db
import controlador
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)


@app.route('/')
def inicio():
    return 'Bienvenido a la API del JNAF n° 1'

@app.route('/expediente/<string:expte>', methods=['GET'])
def expediente_route(expte):
    return controlador.get_expediente(expte)

@app.route('/expedientes/<string:fecha>', methods=['GET'])
def expedientes_route(fecha):
    return controlador.get_expedientes(fecha)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
    
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pablo:lunares241090@db:5432/despachos'