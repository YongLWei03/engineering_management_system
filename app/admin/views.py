# -*- coding: utf-8 -*-

from flask import g, render_template
from flask_login import login_required

from . import admin


@admin.route("/", methods=["GET", "POST"])
@login_required
def index():
    print 'g'*100
    print g.user
    return render_template("admin/index.html")
