# --*-- coding:utf-8 --*--

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email


class Login_form(Form):
    account = StringField("请输入邮箱账号",
                          validators=[InputRequired("不能为空"), Email("邮箱格式不正确")])
    password = PasswordField("请输入密码", validators=[InputRequired("不能为空")])
    submit = SubmitField("登录")
