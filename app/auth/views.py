# --*-- coding:utf-8 --*--

from flask import render_template
from . import auth


@auth.route("/login")
def login():
    render_template("auth/login.html")
