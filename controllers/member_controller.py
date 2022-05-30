from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member

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
    return render_template("members/edit.html", title=f"Edit {member.first_name}", member=member)

@members_blueprint.route("/members/add")
def members_add():
    memberships = membership_repo.select_all()
    return render_template("members/add.html", title="Add Member", memberships=memberships)

@members_blueprint.route("/members/add", methods=['POST'])
def members_add_add():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    membership = request.form['memberships']
    membership = membership_repo.select(membership)
    member = Member(first_name, last_name, membership)
    member_repo.save(member)
    return redirect("/members")

