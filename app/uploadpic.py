from google.appengine.ext import db
import json

class Picture(db.Model):
	picture = db.BlobProperty()
	metadata = db.TextProperty()

	def setPicture(self, filestream):
		self.picture = db.Blob(filestream)
	def setMetadata(self, metadata):
		self.metadata = json.dmpts(metadata)
	def getMetadata(self):
		return json.loads(self.metadata)