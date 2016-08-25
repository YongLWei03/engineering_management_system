# --*-- coding:utf-8 --*--

from flask import render_template
from . import auth
from .forms import Login_form


@auth.route("/login")
def login():
    form = Login_form()
    return render_template("auth/login.html", form=form)
