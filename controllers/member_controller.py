from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.member_repository as member_repo
import repositories.membership_repository as membership_repo

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template('members/index.html', title="Members", members=members)

@members_blueprint.route("/members/<id>")
def members_page(id):
    member = member_repo.select(id)
    return render_template("members/member.html", title=member.first_name, member=member)

@members_blueprint.route("/members/<id>/edit")
def members_edit_view(id):
    member = member_repo.select(id)
    return render_template("members/edit.html", title=f"Edit {member.first_name}", member=member)

@members_blueprint.route("/members/<id>/edit", methods=['POST'])
def members_edit_edit(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    member = member_repo.select(id)
    member.first_name = first_name
    member.last_name = last_name
    member_repo.update(member)
    return render_template("members/edit.html", title=f"Edit {member.first_name}", member=member, firstname=first_name)
