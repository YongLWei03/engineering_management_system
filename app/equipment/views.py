# --*-- coding:utf-8 --*--

import json

from flask import render_template, request
from flask import login_required, current_user

from . import equipment
from app.models import Equipment
from app import db


@equipment.route("/manage/", methods=["GET", "POST"])
@login_required
def equipment():
    user = current_user
    return render_template("equipment/equipment_list.html", user=user)


@equipment.route("/data/", methods=['POST'])
@login_required
def equipment_data():
    r_json = {}

    current = int(request.form["current"])
    rowCount = int(request.form["rowCount"])
    r_json["current"] = current
    r_json["rowCount"] = rowCount

    count = Equipment.get_count()
    all_equipment = Equipment.get_all_user()[
        (current-1)*rowCount: current*rowCount]

    r_json['rows'] = all_equipment
    r_json['total'] = count
    return json.dumps(r_json)


@equipment.route("/edit/", methods=["GET", "POST"])
@login_required
def add_equipment():
    user = current_user
    if request.method == "GET":
        """
        equipment_info = None
        equipment_id = request.args.get('id')
        if equipment_id:
            equipment = User.query.filter_by(id=int(equipment_id)).first()
            equipment_info = equipment.to_dict()
        """
        return render_template("equipment/edit_equipment.html", user=user)
    elif request.method == "POST":
        equipment_id = request.form.get('equipment_id')
        if equipment_id:
            update_dict = request.form.to_dict()
            update_dict.pop('equipment_id')
            equipment_id = int(equipment_id)
            db.session.query(User).filter(
                User.id == equipment_id).update(update_dict)
        else:
            new_user = User(
                email=request.form.get("email"), name=request.form.get("name"),
                mobile=request.form.get("mobile"),
                employee_id=request.form.get("employee_id"),
                gender=request.form.get("gender"),
                position=request.form.get("position"),
                birthday=request.form.get("birthday"), role_id=2)
            db.session.add(new_user)
        return json.dumps({'msg': 'success'})


@equipment.route("/remove/<int:equipment_id>", methods=['GET'])
def remove_equipment(equipment_id):
    equipment = User.query.filter_by(id=equipment_id).first()
    db.session.delete(equipment)
    return 'success'
