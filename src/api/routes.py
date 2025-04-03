"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Client, ProjectManager
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager


api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/signup', methods=['POST'])
def handle_signup():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if ProjectManager.query.filter_by(email=email).first():
        return jsonify({"msg": "this email is already taken"}), 400

    hashed_password = generate_password_hash(password)
    new_project_manager = ProjectManager(email=email, password=hashed_password, is_active=True)

    db.session.add(new_project_manager)
    db.session.commit()

    return jsonify({"msg": "project_manager created successfully"}), 201


@api.route('/login', methods=['POST'])
def handle_login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    project_manager = ProjectManager.query.filter_by(email=email).first()
    if project_manager is None or not check_password_hash(project_manager.password, password):
        return jsonify({"msg": "invalid email or password"}), 401

    expiration = datetime.timedelta(days=7)
    access_token = create_access_token(
        identity=project_manager.email, expires_delta=expiration)
    return jsonify({"token": access_token}), 200
