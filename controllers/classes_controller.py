from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.classes import Classes

import repositories.classes_repository as classes_repo
import repositories.attend_repository as attend_repo
classes_blueprint = Blueprint("classes", __name__)

@classes_blueprint.route("/classes")
def classes():
    classes = classes_repo.select_all()
    return render_template("classes/index.html", title="Classes", classes=classes)

@classes_blueprint.route("/classes/<id>")
def class_view(id):
    class1 = classes_repo.select(id)
    peeps = attend_repo.select_class_return_attendees(id)
    return render_template("classes/class.html", title=class1.name, class1=class1, peeps=peeps)

@classes_blueprint.route("/classes/<id>/edit")
def edit_class_view(id):
    class1 = classes_repo.select(id)
    return render_template("/classes/edit.html", title=f"Edit {class1.name}", class1=class1)

@classes_blueprint.route("/classes/<id>/edit", methods=['POST'])
def edit_class(id):
    class1 = classes_repo.select(id)
    class1.name = request.form['name']
    class1.capacity = request.form['capacity']
    time = request.form['time']
    time = time.replace("T", " ")
    class1.time = time
    classes_repo.update(class1)
    return redirect("/classes")

@classes_blueprint.route("/classes/add")
def classes_add_view():
    return render_template("classes/add.html", title="Add Class")

@classes_blueprint.route("/classes/add", methods=['POST'])
def classes_add():
    name = request.form['name']
    capacity = request.form['capacity']
    time = request.form['time']
    time = time.replace("T", " ")
    class1 = Classes(name, capacity, time)
    classes_repo.save(class1)
    return redirect('/classes')