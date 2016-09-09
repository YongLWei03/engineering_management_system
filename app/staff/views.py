# -*- coding:utf-8 -*-

from flask import render_template, request
from flask_login import login_required, current_user
import json
import traceback

from . import staff
from app.models import Department
from app import db


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


@staff.route("/department/add/", methods=["POST"])
@login_required
def add_department():
    try:
        current_id = request.form["current_id"]
        name = request.form["name"]
        new_dep = Department(name=name, pId=int(current_id))
        db.session.add(new_dep)
        return json.dumps({"info": "success", "new_id": new_dep.id})
    except:
        print traceback.format_exc()
        return json.dumps({"info": "fail"})
