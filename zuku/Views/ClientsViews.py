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

@client_blueprint.route('/list client api', methods=['POST', 'GET'])
def listClientApi():
    clients = []
    client_list = Clients.query.all()
    for client in client_list:
        clients.append({'id':client.id,'username':client.username,'fname':client.fname
                           ,'oname':client.oname,'tel':client.tel,'apart_no':client.apart_no,'floor':client.floor
                           ,'estate':client.estate,'address':client.address,'city':client.city
        })
    return  {"clients":clients}
