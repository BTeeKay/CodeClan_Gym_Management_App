from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.attend_repository as attend_repo
# import repositories.classes_repository as classes_repo
# import repositories.member_repository as member_repo

attending_blueprint = Blueprint("attending", __name__)

@attending_blueprint.route("/attending")
def attending():
    attending = attend_repo.select_all()
    return render_template("attending/index.html", title="Attending", attending=attending)