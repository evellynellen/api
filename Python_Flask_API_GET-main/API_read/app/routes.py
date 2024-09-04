from flask_restful import Resource, reqparse
from app.models import Sensor
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Sensor_modelo(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('tipo')
    argumentos.add_argument('dados')
    
    def get(self):
        return{'Sensor':[senso.json() for senso in Sensor.query.all()]}