from wtforms import StringField, IntegerField, SubmitField
from flask_wtf import FlaskForm

class AddForm(FlaskForm):
    fname = StringField('First Name')
    oname = StringField("Other Name")
    email = StringField("Email")
    tel = StringField("Contact")
    nin = StringField("national ID number")
    apart_no = StringField("Apartment Number")
    floor = StringField("Floor")
    estate = StringField("Estate")
    address = StringField("Address")
    post_code = StringField("Post Code")
    city = StringField("City")
    pfname = StringField("Payers Firt Name")
    poname = StringField("Payers Other Name")
    pemail = StringField("Payers Email")
    ptell = StringField("Payers Contact")
    submit = SubmitField("Submit")
