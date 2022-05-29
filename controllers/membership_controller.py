from flask import Flask, render_template, request, redirect
from flask import Blueprint


memberships_blueprint = Blueprint("memberships", __name__)

@memberships_blueprint.route("/memberships")
def memberships():
    return "Hello, World!"