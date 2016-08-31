# -*- coding: utf-8 -*-

from . import db
from . import login_manager

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    nickname = db.Column(db.String(64))
    #company_id = db.Column(db.Integer)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError("密码是不可读的属性")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    pId = db.Column(db.Integer)
    users = db.relationship('User', backref='department')

    def __init__(self, name, pId):
        self.name = name
        self.pId = pId

    def to_dict(self):
        return {"id": self.id, "pId": self.pId, "name": self.name}


@login_manager.user_loader
def load_user(user_id):
    "加载用户的回调函数"
    return User.query.get(int(user_id))
