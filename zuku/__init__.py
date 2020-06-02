import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


login_manager = LoginManager()
app = Flask(__name__)
CORS(app)
login_manager.init_app(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SECRET_KEY"] = "fljsfjaiofuifvioadfhuefslscdufhcvjkduaweuo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "ZukuDB")
# App.config["SQLALCHEMY_BINDS"] = {"Accounts": "sqlite:///" + os.path.join(basedir, "AccountsDB")}
db = SQLAlchemy(app)
Migrate(app, db)
login_manager.login_view = "login"


from zuku.Views.AccountsViews import account_blueprint
from zuku.Views.ServicesViews import service_blueprint
from zuku.Views.ClientsViews import client_blueprint
from zuku.Views.InstalltioinView import installation_blueprint

app.register_blueprint(account_blueprint, url_prifix='/accounts')
app.register_blueprint(service_blueprint, url_prifix='/services')
app.register_blueprint(client_blueprint, url_prifix='/clients')
app.register_blueprint(installation_blueprint, url_prifix='/installations')
