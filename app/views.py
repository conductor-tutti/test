#-*-coding:utf-8-*-
from flask import render_template, request, redirect, url_for, current_app
from googledb import Files
from app import app
from uploadpic import Picture

import urllib2
import sys
reload(sys)
sys.setdefaultencoding("UTF8")

@app.route("/")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/test_picdata", methods=["GET", "POST"])

def test_picdata():
    if request.method == "POST":
        file = request.files.get("file")
        filestream = file.read()
        picture = Picture()
        picture.setPicture(filestream)
        picture.setMetadata({})
        picture.put()
        return "Great!"
    else:
       return render_template("test_picdata.html")

@app.route("/update", methods=["GET", "POST"])
def db_update():
    if request.files:
        post_data = request.files.get("photo")
        string_data = request.form.get("string")

        filestream = post_data.read()

        upload_data = Files()
        upload_data.photo = db.Blob(filestream)
        upload_data.string = string_data
        upload_data.put()

        url = url_for("display_image", key=upload_data.key())
 
        result = Files.all()

        return render_template("minitwitter.html", url=url, string_data=string_data, result=result)
    return render_template("minitwitter.html")

@app.route("/show/<key>", methods=["GET"])
def display_image(key):
    upload_data = db.get(key)
    return current_app.response_class(upload_data.photo)
