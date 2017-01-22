# --*-- coding:utf-8 --*--

import os
import json

from flask import render_template, request
from flask_login import login_required, current_user
from flask import current_app
from werkzeug.utils import secure_filename

from . import equipment
from app.models import Equipment
from app import db


@equipment.route("/manage/", methods=["GET"])
@login_required
def equipment_manage():
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
    all_equipment = Equipment.get_all_equipment()[
        (current-1)*rowCount: current*rowCount]

    r_json['rows'] = all_equipment
    r_json['total'] = count
    print r_json
    return json.dumps(r_json)


@equipment.route("/edit/", methods=["GET", "POST"])
@login_required
def add_equipment():
    user = current_user
    if request.method == "GET":
        equipment_info = None
        equipment_id = request.args.get('id')
        if equipment_id:
            equipment = Equipment.query.filter_by(id=int(equipment_id)).first()
            equipment_info = equipment.to_dict()
        return render_template("equipment/edit_equipment.html", user=user,
                               equipment_info=equipment_info)
    elif request.method == "POST":
        equipment_id = request.form.get('equipment_id')
        if equipment_id:
            update_dict = request.form.to_dict()
            equipment_info = update_dict
            update_dict.pop('equipment_id')
            equipment_id = int(equipment_id)
            db.session.query(Equipment).filter(
                Equipment.id == equipment_id).update(update_dict)
        else:
            pic = request.files.get('picture')
            if pic:
                filename = secure_filename(pic.filename)
                pic.save(os.path.join(current_app.config['UPLOAD_FOLDER'],
                                      filename))
                picture = "/static/upload/{}".format(filename)
            else:
                picture = ''
            print 'r'*100
            print request.form
            new_equipment = Equipment(
                name=request.form.get("name"),
                picture=picture,
                model=request.form.get("model"),
                number=int(request.form.get("number")),
                profile=request.form.get("profile"),
                buy_date=request.form.get("buy_date"),
                price=float(request.form.get('price')),
                vendor=request.form.get("vendor"),
                status=int(request.form.get('status')))
            db.session.add(new_equipment)
            equipment_info = new_equipment.to_dict()
        return render_template("equipment/edit_equipment.html", user=user,
                               equipment_info=equipment_info)


@equipment.route("/remove/<int:equipment_id>", methods=['GET'])
def remove_equipment(equipment_id):
    equipment = User.query.filter_by(id=equipment_id).first()
    db.session.delete(equipment)
    return 'success'
