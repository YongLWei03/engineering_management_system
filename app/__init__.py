# -*- coding:utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    from admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix="/admin")
    from staff import staff as staff_blueprint
    app.register_blueprint(staff_blueprint, url_prefix="/staff")

    return app
