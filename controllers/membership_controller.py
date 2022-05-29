from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.membership_repository as membership_repo

memberships_blueprint = Blueprint("memberships", __name__)

@memberships_blueprint.route("/memberships")
def memberships():
    memberships = membership_repo.select_all()
    return render_template("memberships/index.html", title="Memberships", memberships=memberships)