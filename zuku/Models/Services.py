from zuku import db


class Services(db.Model):
    __tablename__="Services"
    id = db.Column(db.Integer, primary_key=True, index=True)
    package = db.Column(db.String)
    band = db.Column(db.String)
    amount = db.Column(db.Integer)
    installation = db.relationship("Installations", backref='service installation')

    def __init__(self, package, band, amount):
        self.amount = amount
        self.band = band
        self.package = package


    def __repr__(self):
        return f"{self.package, self.amount, self.band}"
