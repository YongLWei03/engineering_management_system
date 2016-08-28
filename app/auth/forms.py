# --*-- coding:utf-8 --*--

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators


class Login_form(Form):
    email = StringField(u"请输入邮箱账号", [validators.length(min=6, max=35)])
    password = PasswordField(u"请输入密码", [validators.DataRequired()])
    remember_me = BooleanField(u"记住我")
    submit = SubmitField(u"登录")
