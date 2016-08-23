# --*-- coding:utf-8 --*--

from flask import redirect

from . import main


@main.route("/", methods=["GET", "POST"])
def index():
    return redirect("/auth/login")
