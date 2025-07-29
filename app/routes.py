from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .models import db, Task
from .auth import register, login

bp = Blueprint('routes', __name__)

@bp.route('/register', methods=['POST'])
def register_user():
    return register()

@bp.route('/login', methods=['POST'])
def login_user():
    return login()

@bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'done': t.done} for t in tasks])

@bp.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    task = Task(title=data['title'], description=data.get('description'))
    db.session.add(task)
    db.session.commit()
    return jsonify(id=task.id), 201

@bp.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify(message='Updated')

@bp.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify(message='Deleted')