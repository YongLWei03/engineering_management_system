# --*-- coding:utf-8 --*--

from flask import redirect

from . import main


@main.route("/", methods=["GET", "POST"])
def index():
    return redirect("/auth/login")


@main.route("/backend/", methods=["GET"])
def backend():
    return u"杨员外的后端博客"


@main.route("/frontend/", methods=["GET"])
def frontend():
    return u"秋月的前端博客"
