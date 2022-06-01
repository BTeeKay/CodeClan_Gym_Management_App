from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.membership_repository as membership_repo

memberships_blueprint = Blueprint("memberships", __name__)

@memberships_blueprint.route("/memberships")
def memberships():
    memberships = membership_repo.select_all()
    return render_template("memberships/index.html", title="Memberships", memberships=memberships)

@memberships_blueprint.route("/memberships/<id>")
def membership_page(id):
    membership = membership_repo.select(id)
    return render_template("memberships/membership.html", title=membership.level, membership=membership)

@memberships_blueprint.route("/memberships/add")
def memberships_add_view():
    return render_template("memberships/add.html", title="Add Membership")