# -*- coding:utf-8 -*-

from flask import render_template
from flask_login import login_required, current_user
import json

from . import staff
from app.models import Department


@staff.route("/department/", methods=["GET", "POST"])
@login_required
def department():
    user = current_user
    return render_template("staff/department.html", user=user)


@staff.route("/department/get_tree_json/", methods=["GET", "POST"])
@login_required
def get_tree_json():
    query_data = Department.query.all()
    departments = [i.to_dict() for i in query_data]
    return json.dumps(departments)
