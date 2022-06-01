from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.membership_repository as membership_repo

from models.membership import Membership

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

@memberships_blueprint.route("/memberships/add", methods=['POST'])
def memberships_add():
    level = request.form['level']
    description = request.form['description']
    membership = Membership(level, description)
    membership = membership_repo.save(membership) 
    return redirect("/memberships")

@memberships_blueprint.route("/memberships/<id>/edit")
def membership_edit_view(id):
    membership = membership_repo.select(id)
    return render_template("memberships/edit.html", title=f"Edit {membership.level}", membership=membership)

@memberships_blueprint.route("/memberships/<id>/edit", methods=['POST'])
def membership_edit(id):
    membership = membership_repo.select(id)
    level = request.form['level']
    description = request.form['description']
    membership.level = level
    membership.description = description
    membership_repo.update(membership)
    return redirect(f"/memberships/{id}/edit")