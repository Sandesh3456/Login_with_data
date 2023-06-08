from flask import Flask 
import flask 
import string
import secrets
import json


app= Flask(
    __name__,
    static_url_path="",
    template_folder="../UI/templates/",
    static_folder = "../UI/static/",
    )

app.secret_key="duw283rgdwq"


@app.route("/")
@app.route("/homepage")
def home():
    topic = "HELLO EVERYONE"
    return flask.render_template("homepage.html",header=topic)


@app.route("/login")
def login():
    return flask.render_template("login.html",action="/login_post")


@app.route("/login_post", methods = ["POST"])
def post_login():
    name = flask.request.form["username"]
    password = flask.request.form["password"]
    # print(name)
    # print(password)
    if len(name or password) < 9:
        return flask.render_template("errorpage.html")
    else:
        return flask.render_template("Welcomepage.html")


@app.route("/signup")
def signup():
    length=16
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for i in range(length))
    return flask.render_template("signup.html",action="/signup_post") 
 

@app.route("/signup_post", methods = ["POST"])
def post_signup():
    record= []
    name = flask.request.form["username"]
    email_sign= flask.request.form["email_signup"]
    password = flask.request.form["password"]

    signup_data={}
    signup_data["name"]=name;
    signup_data["email_sign"]=email_sign;
    signup_data["password"]=password;
    print(signup_data)

    record.append(signup_data)
    print("record=",record)

    with open("record.py", "a") as outputfile:
        print("output",outputfile)
        json.dump(record, outputfile)


    if len(name or password) < 9:
        return flask.render_template("errorpage.html")
    else:
        return flask.render_template("homepage.html")
