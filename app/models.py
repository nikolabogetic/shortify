from . import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(1000))

    def __repr__(self):
        return '<URL {}>'.format(self.url)