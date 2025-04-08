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
def add_client():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    phone_number = data.get("phone_number")
    about_me = data.get("about_me", "")
    is_active = data.get("is_active", True)

    # Basic validation
    if not all([email, password, first_name, last_name, phone_number]):
        return jsonify({"error": "Missing required fields"}), 400

    # Optional: Check if email already exists
    if Client.query.filter_by(email=email).first():
        return jsonify({"error": "Client with this email already exists"}), 409

    hashed_password = generate_password_hash(password)

    new_client = Client(
        email=email,
        password=hashed_password,
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        about_me=about_me,
        is_active=is_active
    )

    db.session.add(new_client)
    db.session.commit()

    return jsonify(new_client.serialize()), 201

@api.route('/client/<int:id>', methods=['GET'])
def get_client(id):
    client = Client.query.get(id)
    if not client:
        return jsonify({'message': 'Client not found'}), 404
    return jsonify(client.serialize())

@api.route('/client/<int:id>', methods=['PUT'])
def update_client(id):
    data = request.get_json()
    client = Client.query.get(id)
    if not client:
        return jsonify({'message': 'Client not found'}), 404
    for key, value in data.items():
        setattr(client, key, value)
    db.session.commit()
    return jsonify(client.serialize())

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
def add_project_manager():
    data = request.get_json()
    new_manager = ProjectManager(**data)
    db.session.add(new_manager)
    db.session.commit()
    return jsonify(new_manager.serialize()), 201

@api.route('/project-manager/<int:id>', methods=['GET'])
def get_project_manager(id):
    manager = ProjectManager.query.get(id)
    if not manager:
        return jsonify({'message': 'Project Manager not found'}), 404
    return jsonify(manager.serialize())

@api.route('/project-manager/<int:id>', methods=['PUT'])
def update_project_manager(id):
    data = request.get_json()
    manager = ProjectManager.query.get(id)
    if not manager:
        return jsonify({'message': 'Project Manager not found'}), 404
    for key, value in data.items():
        setattr(manager, key, value)
    db.session.commit()
    return jsonify(manager.serialize())

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


