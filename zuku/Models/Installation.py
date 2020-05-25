from zuku import  db


class Installations(db.Model):
    __tablename__='Installations'
    id = db.Column(db.Integer, primary_key=True, index=True)
    client = db.Column(db.Integer, db.ForeignKey("Clients.id"))
    service = db.Column(db.Integer, db.ForeignKey("Services.id"))

    def __repr__(self):
        return f"{self.client,self.service}"
