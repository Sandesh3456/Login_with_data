from flask import Flask 
import flask 
import json
import re

app= Flask(
    __name__,
    static_url_path="",
    template_folder="../UI/templates/",
    static_folder = "../UI/static/",
    )

app.secret_key="duw283rgdwq"


@app.route("/signup")
def signup():
    return flask.render_template("signup.html",action="/signup_post") 
 

@app.route("/signup_post", methods = ["POST"])
def post_signup():
    name = flask.request.form["username"]
    email_sign= flask.request.form["email_signup"]
    password = flask.request.form["password"]

    
    signup_data={}
    signup_data["name"]=name;
    signup_data["email_sign"]=email_sign;
    signup_data["password"]=password;
    print(signup_data)
    print("---")


    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    if re.fullmatch(regex, email_sign):
        print("Valid email")
    else:
        return flask.render_template("errorpage.html")
    if len(name or password) < 9:
        return flask.render_template("errorpage.html")
    

    with open('data.json') as user_file:
        file_contents = user_file.read()

    parsed_json = json.loads(file_contents)
 
    for i in parsed_json['user_records']:
        if (i['email_sign']==email_sign):
            return flask.render_template("errorpage.html")


    def write_json(new_data, filename='data.json'):
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
             # Join new_data with file_data inside emp_details
            file_data["user_records"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
    

    write_json(signup_data)

    return flask.render_template("homepage.html")

@app.route("/")
@app.route("/homepage")
def home():
    topic = "HELLO EVERYONE" 
    return flask.render_template("homepage.html",header=topic)


@app.route("/login")
def login():
    print('Get----')
    return flask.render_template("login.html",action="/login_post")


@app.route("/login_post", methods = ["POST"])
def post_login():
    print('post----')
    email_sign= flask.request.form["email_signup"]
    password = flask.request.form["password"]
    print("name is =",email_sign)
    print("password is =",password)

    with open('data.json') as user_file:
        file_contents = user_file.read()

    parsed_json = json.loads(file_contents)
    print(parsed_json)
    
    for i in parsed_json['user_records']:

        print("here",i["name"], i["password"])
        
        if(i['email_sign']==email_sign and i['password']==password):

            print("signed_email is",i['email_sign'])
            print("signed_password is",i['password'])
            login_status = "True"
        else:
            print("error signed_email is",i['email_sign'])
            print("eeror signed_password is",i['password'])
            login_status = "False"
    if login_status =="True":  
        return flask.render_template("Welcomepage.html") 
    else:
        return flask.render_template("errorpage.html")  


