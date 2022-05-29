from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.classes_repository as classes_repo
classes_blueprint = Blueprint("classes", __name__)

@classes_blueprint.route("/classes")
def classes():
    classes = classes_repo.select_all()
    return render_template("classes/index.html", title="Classes", classes=classes)