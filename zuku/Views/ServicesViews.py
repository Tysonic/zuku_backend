from zuku import db
from flask import render_template, redirect, url_for, Blueprint

from zuku.Forms.Form import AddForm
from zuku.Forms.addServices import AddServices
from zuku.Models.Services import Services

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

@service_blueprint.route('/services list', methods=['POST','GET'])
def listServices():
    services_list=Services.query.all()
    services = []
    for x in services_list:
        services.append({"id":x.id,'band':x.band, 'package':x.package, 'amount':x.amount})

    print(services)
    return {'services':services}



