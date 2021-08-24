from .. import usr
from flask import render_template


@usr.route("/")
def home():
    return render_template("home.html", title="Home")