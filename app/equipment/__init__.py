# --*-- coding:utf-8 --*--

from flask import Blueprint

equipment = Blueprint("equipment", __name__)

from . import views
