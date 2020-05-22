from zuku import db
from flask import request, render_template, url_for, Blueprint
from zuku.Models.Installation import  Installations


installation_blueprint = Blueprint("installations", __name__)

@installation_blueprint.route("/instations", methods =['GET','POST'])
def installations():
    new = Installations(client=1, service=1)
    db.session.add(new)
    db.session.commit()
    return render_template('installations.html')
    
