"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Client, ProjectManager, Invoice
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager


api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

# CLIENT ROUTES
@api.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify([client.serialize() for client in clients])

@api.route('/add-client', methods=['POST'])
def create_client():
    email= request.json.get("email",None)
    password= request.json.get("password",None)
    is_active= request.json.get("is_active",None)
    first_name= request.json.get("first_name",None)
    last_name= request.json.get("last_name",None)
    phone_number= request.json.get("phone_number",None)
    about_me= request.json.get("about_me",None)
    if email is None or password is None or is_active is None or first_name is None or last_name is None or phone_number is None or about_me is None:    
        return jsonify({"msg":"some fields are missing in your request"}), 400

    client=Client.query.filter_by(email=email).one_or_none()

    if client:
        return jsonify({"msg":"account associted with that email already exists"}), 409
    client=Client(email=email,password=password,is_active=True,first_name=first_name,last_name=last_name,phone_number=phone_number,about_me=about_me)
    db.session.add(client)
    db.session.commit()
    response_body={"msg":"client successfully created","client":client.serialize()}
    return jsonify(response_body), 201

@api.route('/client/<int:id>', methods=['GET'])
def get_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({'message': 'Client not found'}), 404
    return jsonify(client.serialize())

@api.route('/client/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    email= request.json.get("email")
    first_name= request.json.get("first_name")
    last_name= request.json.get("last_name")
    phone_number= request.json.get("phone_number")
    about_me= request.json.get("about_me")
    if email is None or first_name is None or last_name is None or phone_number is None or about_me is None:    
        return jsonify({"msg":"some fields are missing in your request"}), 400

    client=Client.query.filter_by(id=client_id).one_or_none()

    if client is None:
        return jsonify({"msg":"no client found"}), 404
    client.email=email
    client.first_name=first_name
    client.last_name=last_name
    client.phone_number=phone_number
    client.about_me=about_me
    db.session.commit()
    db.session.refresh(client)
    response_body={"msg":"client successfully edited","client":client.serialize()}
    return jsonify(response_body), 201  


@api.route('/client/<int:id>', methods=['DELETE'])
def delete_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({'message': 'Client not found'}), 404
    db.session.delete(client)
    db.session.commit()
    return jsonify({'message': 'Client deleted'})

# PROJECT MANAGER ROUTES
@api.route('/project-managers', methods=['GET'])
def get_project_managers():
    managers = ProjectManager.query.all()
    return jsonify([manager.serialize() for manager in managers])

@api.route('/project-manager', methods=['POST'])
def create_project_manager():
    email= request.json.get("email",None)
    password= request.json.get("password",None)
    is_active= request.json.get("is_active",None)
    first_name= request.json.get("first_name",None)
    last_name= request.json.get("last_name",None)
    skills= request.json.get("skills",None)
    phone_number= request.json.get("phone_number",None)
    experience= request.json.get("experience",None)
    if email is None or password is None or is_active is None or first_name is None or last_name is None or phone_number is None or skills is None or experience is None:    
        return jsonify({"msg":"some fields are missing in your request"}), 400
    
    project_manager=ProjectManager.query.filter_by(email=email).one_or_none()

    
    if project_manager:
        return jsonify({"msg":"account associted with that email already exists"}), 409
    project_manager=ProjectManager(email=email,password=password,is_active=True,experience=experience,first_name=first_name,last_name=last_name,phone_number=phone_number,skills=skills)
    db.session.add(project_manager)
    db.session.commit()
    response_body={"msg":"projectmanager successfully created","projectmanager":project_manager.serialize()}
    return jsonify(response_body), 201

@api.route('/project-manager/<int:id>', methods=['GET'])
def get_project_manager(id):
    manager = ProjectManager.query.get(id)
    if not manager:
        return jsonify({'message': 'Project Manager not found'}), 404
    return jsonify(manager.serialize())

@api.route('/project-manager/<int:project_manager_id>', methods=['PUT'])
def update_project_manager(project_manager_id):
    email= request.json.get("email")
    first_name= request.json.get("first_name")
    last_name= request.json.get("last_name")
    phone_number= request.json.get("phone_number")
    skills= request.json.get("skills")
    experience= request.json.get("experience")
    if email is None or first_name is None or last_name is None or phone_number is None or skills is None or experience is None:    
        return jsonify({"msg":"some fields are missing in your request"}), 400

    project_manager=ProjectManager.query.filter_by(id=project_manager_id).one_or_none()

    if project_manager is None:
        return jsonify({"msg":"no project_manager found"}), 404
    project_manager.email=email
    project_manager.first_name=first_name
    project_manager.last_name=last_name
    project_manager.phone_number=phone_number
    project_manager.skills=skills
    project_manager.experience=experience
    db.session.commit()
    db.session.refresh(project_manager)
    response_body={"msg":"project_manager successfully edited","project_manager":project_manager.serialize()}
    return jsonify(response_body), 201  



@api.route('/project-manager/<int:id>', methods=['DELETE'])
def delete_project_manager(id):
    manager = ProjectManager.query.get(id)
    if not manager:
        return jsonify({'message': 'Project Manager not found'}), 404
    db.session.delete(manager)
    db.session.commit()
    return jsonify({'message': 'Project Manager deleted'})

# INVOICE ROUTES
@api.route('/invoices', methods=['GET'])
def get_invoices():
    invoices = Invoice.query.all()
    return jsonify([invoice.serialize() for invoice in invoices])

@api.route('/invoice', methods=['POST'])
def add_invoice():
    data = request.get_json()
    new_invoice = Invoice(**data)
    db.session.add(new_invoice)
    db.session.commit()
    return jsonify(new_invoice.serialize()), 201

@api.route('/invoice/<int:id>', methods=['GET'])
def get_invoice(id):
    invoice = Invoice.query.get(id)
    if not invoice:
        return jsonify({'message': 'Invoice not found'}), 404
    return jsonify(invoice.serialize())

@api.route('/invoice/<int:id>', methods=['PUT'])
def update_invoice(id):
    data = request.get_json()
    invoice = Invoice.query.get(id)
    if not invoice:
        return jsonify({'message': 'Invoice not found'}), 404
    for key, value in data.items():
        setattr(invoice, key, value)
    db.session.commit()
    return jsonify(invoice.serialize())

@api.route('/invoice/<int:id>', methods=['DELETE'])
def delete_invoice(id):
    invoice = Invoice.query.get(id)
    if not invoice:
        return jsonify({'message': 'Invoice not found'}), 404
    db.session.delete(invoice)
    db.session.commit()
    return jsonify({'message': 'Invoice deleted'})


