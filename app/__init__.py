from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    import app.routes as r

    app.register_blueprint(r.auth_bp, url_prefix="/api/auth")
    app.register_blueprint(r.user_bp, url_prefix="/api/user")

    return app


from app import models as m
