from zuku import db
from flask import request, render_template, url_for, Blueprint
from zuku.Models.Installation import  Installations
from zuku.Models.Clients import Clients
from zuku.Models.Services import Services

installation_blueprint = Blueprint("installations", __name__)

@installation_blueprint.route("/installations", methods =['POST'])
def installations():

    form = request.json
    new = Installations(client=form['client'], service=form['service'])
    db.session.add(new)
    db.session.commit()
    return form

@installation_blueprint.route("/list installations")
def installationList():
    installations = Installations.query.all()
    return  render_template('listInstallations.html', installations=installations)
    
@installation_blueprint.route('/installation details', methods=['POST','GET'])
def installationDetails():
    form = request.json

    client = Clients.query.filter_by(username='Tysonic').first()
    installation = Installations.query.filter_by(client=client.id).first()
    service = Services.query.filter_by(id=installation.service).first()
    return {"client":client, 'installation':installation,'service':service}
