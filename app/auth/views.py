# -*- coding: utf-8 -*-

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user

from . import auth
from ..models import User


@auth.route("/login", methods=["GET", "POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user and user.verify_password(password):
        login_user(user)
        return redirect(request.args.get("next") or url_for("admin.index"))
    flash("用户名或者密码错误")
    return render_template("auth/login.html")
