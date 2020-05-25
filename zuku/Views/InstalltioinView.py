from zuku import db
from flask import request, render_template, url_for, Blueprint
from zuku.Models.Installation import  Installations


installation_blueprint = Blueprint("installations", __name__)

@installation_blueprint.route("/installations", methods =['POST'])
def installations():

    form = request.json
    new = Installations(client=form['client'], service=form['service'])
    db.session.add(new)
    db.session.commit()
    return form
    
