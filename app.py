from flask import Flask, render_template, send_from_directory
import os

from controllers.member_controller import members_blueprint
from controllers.attending_controller import attending_blueprint
from controllers.classes_controller import classes_blueprint
from controllers.membership_controller import memberships_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(memberships_blueprint)
app.register_blueprint(attending_blueprint)
app.register_blueprint(classes_blueprint)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

if __name__ == '__main__':
    app.run(debug=True)