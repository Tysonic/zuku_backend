from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddServices(FlaskForm):

    package = StringField("Package")
    band = StringField('Band')
    amount = IntegerField("Amount")

    submit = SubmitField("Submit")
