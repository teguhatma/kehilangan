from .. import admin
from flask import render_template
from flask_login import login_required


@admin.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", title="Dashboard")