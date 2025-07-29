from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from .models import db, User

def register():
    data = request.get_json()
    hashed = generate_password_hash(data['password'])
    new_user = User(username=data['username'], password=hashed)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User created"), 201

def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify(message="Invalid credentials"), 401