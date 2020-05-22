from wtforms import StringField, IntegerField, SubmitField
from flask_wtf import FlaskForm

class AddForm(FlaskForm):
    username = StringField("UserName")
    email = StringField('Email')
    password = StringField('Password')
    package = StringField("Package")
    band = StringField('Band')
    add_charge = StringField("Additional Charge")
    amount = IntegerField("Amount")

    submit = SubmitField("Submit")

