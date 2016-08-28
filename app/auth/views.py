# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user

from . import auth
from .forms import Login_form
from ..models import User


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = Login_form()
    print 'f'*100
    print form.validate_on_submit()
    print form.email.data
    print form.password.data
    if form.validate_on_submit():
        print 'f'*100
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get("next") or url_for("main.index"))
        flash("用户名或者密码错误")
    return render_template("auth/login.html", form=form)
