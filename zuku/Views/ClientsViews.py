from flask import render_template, redirect, url_for, Blueprint
from zuku import  db
from zuku.Forms.clientForm import  AddForm
from flask import request
from zuku.Models.Clients import Clients

client_blueprint = Blueprint("clients", __name__)

@client_blueprint.route('/add client', methods = ['POST', 'GET'])
def addClients():

    form = request.json
    if form.validate_on_submit():
        Clients.query.filter_by(username=form['username']).update(dict(fname = form['fname'],oname = form['oname'],
                             tel = form['tel'],apart_no = form['apart_no'], floor =form['floor'],estate =form['estate'],address = form['address'],
                             city = form['city']))
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('clients.listClients'))

    return render_template('add.html', form=form)




@client_blueprint.route('/list clients', methods=['POST','GET'])
def listClients():
    return render_template('clientsList.html', clients = Clients.query.all())

@client_blueprint.route('/list client api')
def listClientApi():
    return  {"clients":Clients.query.all()}
