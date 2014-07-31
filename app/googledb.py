from google.appengine.ext import db


class Files(db.Model):
    photo = db.BlobProperty()
    string = db.StringProperty()