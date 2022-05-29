from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.member_repository as member_repo


members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repo.select_all()
    return render_template('members/index.html', title="Members", members=members)