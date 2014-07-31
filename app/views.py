#-*-coding:utf-8-*-

import urllib
from bs4 import BeautifulSoup

from flask import render_template, request, redirect, url_for, current_app
from app import app

import sys
reload(sys)
sys.setdefaultencoding("UTF8")

from flaskext import wtf
from flaskext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError


from google.appengine.ext import db

class Files(db.Model):
    photo = db.BlobProperty()
    string = db.StringProperty()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/tutti")
def tutti():
    return render_template("tutti.html")

@app.route("/minitwitter", methods=["POST"])
def minitwitter():
    if request.method == "POST":
        if request.form.get("minitwitter"):
            return render_template("minitwitter.html")
        else:
            return render_template("index.html")
    return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_query = request.form.get("search_query")
        if request.form.get("search_google"):
            return redirect("https://www.google.co.kr/q=" + search_query)
        elif request.form.get("search_naver"):
            return redirect("http://search.naver.com/search.naver?query=" + search_query)
        elif request.form.get("search_daum"):
            return redirect("http://search.daum.net/search?q=" + search_query)
        else:
            return render_template("index.html", search_query=search_query)
    else:
        return render_template("index.html", search_query=search_query)


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        calculate_num1 = request.form.get("calculate_num1")
        calculate_num2 = request.form.get("calculate_num2")
        operator_sum = request.form.get("operator_sum")
        result_calculate = int(calculate_num1) + int(calculate_num2)
        return render_template("index.html", result_calculate=result_calculate)
    else:
        return render_template("index.html")

@app.route("/gugu", methods=["GET", "POST"])
def gugu():
    input_gugu = request.form.get("input_gugu")
    list_result = []
    if request.method == "POST":
        for i in range(1, 10):
            result = int(input_gugu) * i
            list_result.append(str(input_gugu) + "x" + str(i) + "=" + str(result))
        return render_template("index.html", list_result=list_result)
    else:
        return render_template("index.html")
    
@app.route("/to_crawl", methods=["GET", "POST"])
def to_crawl():
    if request.method == "POST":
        crawl_link = request.form.get("crawl_link")
        if request.form.get("crawl_link"):
            return render_template("crawl.html")
        else:
            return render_template("index.html")


@app.route("/crawl", methods=["GET", "POST"])
def crawl():
    if request.method == "POST":
        huntURL = request.form.get("huntURL")
        if request.form.keys():
            if "http://" not in huntURL:
                huntURL = "http://" + huntURL
            else:
                huntURL = huntURL
            htmlsource = urllib.urlopen(huntURL).read()
            soup = BeautifulSoup(htmlsource)
            return render_template("crawl.html", inputURL=huntURL, crawl_result=soup.head)
        else:
            return render_template("crawl.html", inputURL=None, crawl_result="아직 보여줄게 없어요.")
    else:
        return render_template("crawl.html", inputURL=None, crawl_result="아직 보여줄게 없어요.")


class SearchNews(Form):
    category = TextField("Category", [validators.Required("정치, 사회, 경제 중 한 가지 값만 주세요.")])   
    submit = SubmitField("Send")
    list_category = ["정치", "경제", "사회"]
    def validate_category(field):
        if field not in list_category:
            return 0
            # raise ValidationError("정치, 사회, 경제 중 한 가지 값만 주세요.")
        else:
            return 1
@app.route("/validate", methods=["GET", "POST"])
def validate():
    
    form = SearchNews()
    if request.method == "POST":
        if not form.validate_category(form.category.data):
            return render_template("validate.html", form=form, test="fail")
        else:
            return render_template("index.html", form=form, test="success")
    return render_template("validate.html", form=form)

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


"""
@app.route("/chu", methods=["GET", "POST"])
def chu():
	get_value = None
	post_value = None
	engine = None

	text_search = request.form.get("text_search")

	if request.method == "GET":
		get_value = request.args.get('message-chu')

	elif request.method == "POST":
		post_value = request.form.get('message-kiss')


	if request.form.get("google"):
		return redirect("http://www.google.com/q=" + text_search)
		
	elif request.form.get("naver"):
		return redirect("http://search.naver.com/search.naver?query=" + text_search)

	elif request.form.get("daum"):
		return redirect("http://search.daum.net/search?q=" + text_search)

	else:
		return render_template("chu.html", get_value = get_value, post_value = post_value)
"""
