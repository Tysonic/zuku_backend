from zuku import db


class Accounts(db.Model):
    __tablename__="Accounts"
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email = db.Column(db.String)

    def __int__(self, username, password, email):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.username, self.password, self.email}"
