# --*-- coding:utf-8 --*--

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email


class BaseForm(Form):
    LANGUAGES = ['zh']


class Login_form(BaseForm):
    email = StringField(u"请输入邮箱账号", validators=[Required(u"不能为空"), Email(u"邮箱格式不正确")])
    password = PasswordField(u"请输入密码", validators=[Required(u"不能为空")])
    remember_me = BooleanField(u"记住我")
    submit = SubmitField(u"登录")
