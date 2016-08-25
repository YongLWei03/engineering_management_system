# --*-- coding:utf-8 --*--

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email


class BaseForm(Form):
    LANGUAGES = ['zh']


class Login_form(BaseForm):
    account = StringField(u"请输入邮箱账号",
                          validators=[InputRequired(u"不能为空"),
                                      Email(u"邮箱格式不正确")])
    password = PasswordField(u"请输入密码", validators=[InputRequired(u"不能为空")])
    submit = SubmitField(u"登录")
