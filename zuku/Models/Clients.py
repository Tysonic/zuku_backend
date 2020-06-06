from zuku import db


class Clients(db.Model):
    __tablename__ = "Clients"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String)
    installation = db.relationship("Installations", backref='installations')
    fname = db.Column(db.String)
    oname = db.Column(db.String)
    tel = db.Column(db.String)
    apart_no = db.Column(db.String)
    floor = db.Column(db.String)
    estate = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)

    def __init__(self, username,fname=" ", oname=" ",tel=" ", apart_no=" ",floor=" ",estate=" ",address=" ",city=" " ):
        self.username=username
        self.fname=fname
        self.oname=oname
        self.tel=tel
        self.apart_no = apart_no
        self.floor=floor
        self.estate=estate
        self.address=address
        self.city=city

    def __repr__(self):
        return f"{self.id, self.oname, self.tel, self.nin, self.apart_no, self.floor, self.estate, self.address, self.city}"
