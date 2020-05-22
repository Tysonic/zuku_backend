from werkzeug.utils import redirect
from werkzeug.security import  generate_password_hash, check_password_hash

from zuku import db
from flask import request, Blueprint, render_template, url_for
from zuku.Forms.Form import  AddForm
from zuku.Models.Accounts import Accounts

account_blueprint = Blueprint('accounts',__name__)

@account_blueprint.route("/lists", methods=['GET','POST'])
def lists():
    users = Accounts.query.all()
    return render_template("lists.html", users=users)


@account_blueprint.route('/register', methods=['GET','POST'])
def register():
    form = AddForm()
    if form.validate_on_submit():
        user = Accounts(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('accounts.lists'))
    return render_template('add.html', form=form)

