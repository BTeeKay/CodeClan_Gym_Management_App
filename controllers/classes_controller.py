from flask import Flask, render_template, request, redirect
from flask import Blueprint


classes_blueprint = Blueprint("classes", __name__)

@classes_blueprint.route("/classes")
def classes():
    return "Hello, World!"