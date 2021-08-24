from ... import usr
from app import db
from flask import render_template, redirect, url_for, flash, request
from ...form.forms import LoginForm, SignUpForm
from flask_login import login_user, login_required, current_user, logout_user
from app.models import User


@usr.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin.dashboard"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            if next is None or not next.startswith("/"):
                if user:
                    next = url_for("admin.dashboard")
            return redirect(next)
        elif user is None:
            flash("Sorry, no account detected.", "info")
        else:
            flash("Wrong email and password.", "info")
    return render_template("login.html", title="Login", form=form)


@usr.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.generate_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created.")
        return redirect(url_for(".login"))
    return render_template("signup.html", form=form, title="Sign Up")


@usr.route("/logout")
def logout():
    logout_user()
    return redirect(url_for(".login"))
