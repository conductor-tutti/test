#-*-coding:utf-8-*-
from flask import render_template, request, redirect, url_for, current_app
from uploadpic import Picture
from app import app

import urllib2
import sys
reload(sys)
sys.setdefaultencoding("UTF8")

@app.route("/")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/test_picdata", methods=["GET", "POST"])
def picdata():
    if request.method == "POST":
        file = request.files.get("file")
        filestream = file.read()
        picture = Picture()
        picture.setPicture(filestream)
        picture.setMetadata({})
        picture.put()
        return redirect(url_for("display_pic", key=picture.key()))
    else:
       return render_template("test_picdata.html")

@app.route("/show/<key>", methods=["GET"])
def display_pic(key):
    uploadedPic = db.get(key)

    picInfo = {}
    picInfo["picURL"] = url_for("img", key=key)
    picInfo["picMetadata"] = uploadedPic.getMetadata()
    return current_app.response_class(upload_data.photo)



# @app.route("/update", methods=["GET", "POST"])
# def db_update():
#     if request.files:
#         post_data = request.files.get("photo")
#         string_data = request.form.get("string")

#         filestream = post_data.read()

#         upload_data = Files()
#         upload_data.photo = db.Blob(filestream)
#         upload_data.string = string_data
#         upload_data.put()

#         url = url_for("display_image", key=upload_data.key())
 
#         result = Files.all()

#         return render_template("minitwitter.html", url=url, string_data=string_data, result=result)
#     return render_template("minitwitter.html")
# # 