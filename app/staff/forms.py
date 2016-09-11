# --*-- coding:utf-8 --*--

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, \
        HiddenField, validators


class staff_form(Form):
    username = StringField(u"账号", [validators.DataRequired()])
    nickname = StringField(u"昵称", [validators.DataRequired()])
    dep_name = StringField(u"部门", [validators.DataRequired()])
    dep_id = HiddenField(u"部门id", [validators.DataRequired()])
    email = StringField(u"邮箱", [validators.Email()])
    password = PasswordField(
        u"密码", [validators.DataRequired(),
                    validators.EqualTo("confirm", message=u"密码不匹配")])
    confirm = PasswordField(u"确认密码", [validators.DataRequired()])
    submit = SubmitField(u"登录")
