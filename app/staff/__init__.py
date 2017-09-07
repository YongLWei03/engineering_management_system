# -*- coding:utf-8 -*-

from flask import Blueprint

staff = Blueprint("staff", __name__)

from . import views
