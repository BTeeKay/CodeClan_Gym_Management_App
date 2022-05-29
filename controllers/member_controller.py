from flask import Flask, render_template, request, redirect
from flask import Blueprint


members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    return "Hello, World!"