from flask import jsonify
from sqlalchemy import text
from model import db

def get_expediente(expte):
    expte = expte.replace('-', '/')
    query = text("SELECT \"Fecha\", \"Orden\" FROM despachos WHERE \"Expediente\" = :expte ORDER BY \"Fecha\" ASC")
    result = db.session.execute(query, {'expte': expte})
    rows = result.fetchall()
    if not rows:
        return jsonify({'mensaje': 'Expediente no encontrado'}), 404

    return jsonify([{
        'Fecha': str(row.Fecha),
        'Orden': row.Orden,
    } for row in rows])

def get_expedientes(fecha):
    fecha = fecha.replace('-', '/')
    query = text("SELECT \"Orden\", \"Expediente\", \"Caratula\" FROM despachos WHERE \"Fecha\" = :fecha")    
    result = db.session.execute(query, {'fecha': fecha})
    rows = result.fetchall()
    if not rows:
        return jsonify({'mensaje': 'No se encontraron expedientes para esta fecha'}), 404

    return jsonify([{
        'Orden': row.Orden,
        'Expediente': row.Expediente,
        'Caratula': row.Caratula,
    } for row in rows])

