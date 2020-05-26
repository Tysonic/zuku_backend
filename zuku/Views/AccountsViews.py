from flask import url_for, request, render_template, flash, Blueprint
from flask_login import logout_user, login_required, login_user
from werkzeug.routing import ValidationError
from zuku import db
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect
import re
from zuku.Forms.AccountsForms import UserLoginForm, UserRegitrationForm
from zuku.Models.Accounts import Accounts
from zuku.Models.Clients import Clients

account_blueprint = Blueprint('users', __name__, template_folder="templates")

@account_blueprint.route("/login page", methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    try:
        if form.validate_on_submit():
            user = Accounts.query.filter_by(email=form.email.data).first()
            if user is not None and check_password_hash(user.password_hash, form.password.data) :

                login_user(user)
                flash("logged in successfully")
                next = request.args.get("next")

                if next == None or not next[0] == '/':
                    next = url_for("index")
            else:
                raise ValidationError("Password or username is incorrect ")
            return redirect(next)

        return render_template("login.html", form=form)
    except Exception as e:

        return render_template("login.html", form=form, error =e)



@account_blueprint.route("/logout user")
@login_required
def logout():
    logout_user()
    flash("logged out successfully")
    return redirect(url_for("index"))


@account_blueprint.route("/registration page", methods=["GET", "POST"])
def register():
    form = UserRegitrationForm()
    try:

        if form.validate_on_submit():

            if Accounts.query.filter_by(email=form.email.data).first():
                raise ValidationError("your email has already been registered")
            if Accounts.query.filter_by(username=form.username.data).first():
                raise ValidationError("The User Name has already been taken Please Choose another name")
            if len(form.password.data)<8:
                raise ValidationError("Password must be at least 8 characters long")
            if not re.search(r"[\d]+", form.password.data):
                raise ValidationError("This password must contain at least 1 digit")
            if not re.search(r"[A-Z]+", form.password.data):
                print(form.password.data)
                raise ValidationError("This password must contain at least 1 uppercase character")

            new_user = Accounts(username=form.username.data, email=form.email.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash("Registered successfully  ")
            return redirect(url_for("users.login"))
        return render_template("register.html", form=form)
    except Exception as e:
        return render_template("register.html", error=e, form=form)


@account_blueprint.route("/register client", methods=["GET", "POST"])
def registerClient():
    form = request.json

    if Accounts.query.filter_by(email=form["email"]).first():
        return {'result' : "your email has already been registered"}
    if Accounts.query.filter_by(username=form["username"]).first():
        return {'result':"The User Name has already been taken Please Choose another name"}
    new_user = Accounts(username=form['username'], email=form['email'], password=form['password'])
    db.session.add(new_user)
    new_client = Clients(username = form['username'])
    db.session.add(new_client)
    db.session.commit()

    return {'result':'success'}



@account_blueprint.route("/client login", methods=['GET', 'POST'])
def clientLogin():
    form = request.json

    user = Accounts.query.filter_by(email=form['email']).first()
    if user is not None and check_password_hash(user.password_hash, form['password']) :
        login_user(user)
        return {'result':"success"}
    else:
        return {"result":"failed"}

