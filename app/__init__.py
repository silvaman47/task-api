from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['JWT_SECRET_KEY'] = 'super-secret-key'
    db.init_app(app)
    jwt.init_app(app)
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)
    return app