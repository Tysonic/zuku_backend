from flask import render_template, redirect, url_for, Blueprint
from zuku import  db
from zuku.Forms.clientForm import  AddForm
from zuku.Models.Clients import Clients

client_blueprint = Blueprint("clients", __name__)

@client_blueprint.route('/add client', methods = ['POST', 'GET'])
def addClients():
    form = AddForm()
    if form.validate_on_submit():
        new_client = Clients(user = 1,fname = form.fname.data,oname = form.oname.data,email =form.email.data,
                             tel = form.tel.data,nin = form.nin.data,apart_no = form.apart_no.data,
                             floor =form.floor.data,estate =form.estate.data,address = form.address.data,post_code = form.post_code.data,
                             city = form.city.data,pfname = form.pfname.data, poname = form.poname.data,pemail = form.pemail.data,
                             ptell = form.ptell.data)
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('clients.listClients'))

    return render_template('add.html', form=form)

@client_blueprint.route('/list clients', methods=['POST','GET'])
def listClients():
    return render_template('lists.html', clients = Clients.query.all())
