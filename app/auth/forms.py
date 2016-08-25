# --*-- coding:utf-8 --*--

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email


class BaseForm(Form):
    LANGUAGES = ['zh']


class Login_form(BaseForm):
    account = StringField(validators=[Required(u"不能为空"), Email(u"邮箱格式不正确")])
    password = PasswordField(validators=[Required(u"不能为空")])
    submit = SubmitField(u"登录")
