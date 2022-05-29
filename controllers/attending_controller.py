from flask import Flask, render_template, request, redirect
from flask import Blueprint


attending_blueprint = Blueprint("attending", __name__)

@attending_blueprint.route("/attending")
def attending():
    return "Hello, World!"