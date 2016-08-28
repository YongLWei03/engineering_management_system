# -*- coding: utf-8 -*-

from flask import g, render_template
from flask_login import login_required

from . import admin


@admin.route("/", methods=["GET", "POST"])
@login_required
def index():
    return render_template("admin/index.html")
