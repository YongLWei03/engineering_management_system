# -*- coding:utf-8 -*-

from flask import render_template, request
from flask_login import login_required, current_user
import json
import traceback

from . import staff
from app.models import Department, User
from app import db


@staff.route("/manage/", methods=["GET", "POST"])
@login_required
def department():
    user = current_user
    return render_template("staff/staff_list.html", user=user)


@staff.route("/data/", methods=['POST'])
@login_required
def staff_data():
    r_json = {}

    current = int(request.form["current"])
    rowCount = int(request.form["rowCount"])
    r_json["current"] = current
    r_json["rowCount"] = rowCount

    count = User.get_count()
    all_staff = User.get_all_user()[(current-1)*rowCount: current*rowCount]

    r_json['rows'] = all_staff
    r_json['total'] = count
    return json.dumps(r_json)


@staff.route("/edit/<int:staff_id>", methods=["GET", "POST"])
@login_required
def add_staff(staff_id):
    user = current_user
    if request.method == "GET":
        staff_info = None
        if staff_id:
            staff = User.query.filter_by(id=staff_id).first()
            staff_info = staff.to_dict()
        return render_template("staff/edit_staff.html", user=user,
                               staff_info=staff_info)
    elif request.method == "POST":
        new_user = User(
            email=request.form.get("email"), name=request.form.get("name"),
            mobile=request.form.get("mobile"),
            employee_id=request.form.get("employee_id"),
            gender=request.form.get("gender"),
            position=request.form.get("position"),
            birthday=request.form.get("birthday"), role_id=2)
        db.session.add(new_user)
        return json.dumps({'msg': 'success'})


@staff.route("/remove/<int:staff_id>", methods=['GET'])
def remove_staff(staff_id):
    staff = User.query.filter_by(id=staff_id).first()
    db.session.delete(staff)
    return 'success'


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


@staff.route("/department/rename/", methods=["POST"])
@login_required
def rename_department():
    try:
        dep_id = request.form["dep_id"]
        new_name = request.form["name"]
        dep = Department.query.get(int(dep_id))
        dep.name = new_name
        db.session.add(dep)
        return json.dumps({"info": "success"})
    except:
        print traceback.format_exc()
        return json.dumps({"info": u"修改失败"})


@staff.route("/department/remove/", methods=["POST"])
@login_required
def remove_department():
    try:
        dep_id = request.form["dep_id"]
        dep = Department.query.get(int(dep_id))
        print 'u'*100
        print dep.users
        if dep.users:
            return json.dumps({"info": u"此部门下有员工，不能删除"})
        db.session.delete(dep)
        return json.dumps({"info": "success"})
    except:
        return json.dumps({"info": u"删除失败"})
