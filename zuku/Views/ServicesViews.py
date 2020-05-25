from zuku import db
from flask import render_template, redirect, url_for, Blueprint

from zuku.Forms.Form import AddForm
from zuku.Forms.addServices import AddServices
from zuku.Models.Services import Services

from zuku.Models.Clients import Clients

service_blueprint = Blueprint("services", __name__)


@service_blueprint.route('/services', methods=['POST', 'GET'])
def services():
    form = AddServices()
    if form.validate_on_submit():
        new_service = Services(package=form.package.data, band=form.band.data, amount=form.amount.data,)
        db.session.add(new_service)
        db.session.commit()
        return redirect(url_for('services.services'))
    return render_template("services.html", form = form,services=Services.query.all())

@service_blueprint.route('/services list', methods=['GET'])
def listServices():
    services_list=Services.query.all()
    clients_list = Clients.query.all()
    services = []
    clients = []
    for x in services_list:
        services.append({"id":x.id,'band':x.band, 'package':x.package, 'amount':x.amount})
    for client in clients_list:
        clients.append({
                'username':client.username,'email':client.email,'fname':client.fname, 'oname':client.oname
            ,'tel':client.tell,'apart_no':client.apart_no,'floor':client.floor,'estate':client.estate,'address':client.address
            ,'city':client.city
        })

    return {'services':services,'clients':clients}



