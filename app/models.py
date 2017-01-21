# -*- coding: utf-8 -*-

from . import db
from . import login_manager

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import func


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    name = db.Column(db.String(64))
    mobile = db.Column(db.String(20))
    employee_id = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    position = db.Column(db.String(30))
    birthday = db.Column(db.DateTime)
    remark = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError(u"密码是不可读的属性")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        if self.gender == 1:
            gender = u'男'
        else:
            gender = u'女'
        return {
            'id': self.id,
            'email': self.email or '',
            'name': self.name or '',
            'mobile': self.mobile or '',
            'employee_id': self.employee_id or '',
            'gender': gender,
            'birthday': str(self.birthday) or '',
            "remark": self.remark or ''
        }

    @classmethod
    def get_count(cls):
        query = db.session.query(func.count(cls.id)).first()
        return int(query[0])

    @classmethod
    def get_all_user(cls):
        query = db.session.query(cls).all()
        return [i.to_dict() for i in query]


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


class Equipment(db.Model):
    __tablename__ = 'equipments'
    id = db.Column(db.Integer, primary_key=True)
    # 名称
    name = db.Column(db.String(64))
    # 图片
    picture = db.Column(db.String(64))
    # 型号
    model = db.Column(db.String(64))
    # 编号
    number = db.Column(db.Integer)
    # 简介
    profile = db.Column(db.Text)
    # 购买日期
    buy_date = db.Column(db.Date)
    # 价格
    price = db.Column(db.Float)
    # 厂商
    vendor = db.Column(db.String(64))
    # 状态，1正常，2禁用，3维修中，4借出，5报废
    status = db.Column(db.SmallInteger)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'picture': self.picture,
            'model': self.model,
            'number': self.number,
            'profile': self.profile,
            'buy_date': self.buy_date,
            'price': self.price,
            'vendor': self.vendor,
            'status': self.status
        }

    @classmethod
    def get_count(cls):
        query = db.session.query(func.count(cls.id)).first()
        return int(query[0])

    @classmethod
    def get_all_equipment(cls):
        query = db.session.query(cls).all()
        return [i.to_dict() for i in query]
