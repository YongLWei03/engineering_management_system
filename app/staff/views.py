# -*- coding:utf-8 -*-

from flask import render_template
from flask_login import login_required, current_user

from . import staff


@staff.route("/department/", methods=["GET", "POST"])
@login_required
def department():
    user = current_user
    return render_template("admin/index.html", user=user)
