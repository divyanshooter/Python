from flask import Flask,render_template,request,redirect
from db import Database

dbo=Database()

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration',methods=['post'])
def perform_registration():
      name=request.form.get('name')
      email=request.form.get('email')
      password=request.form.get('password')
      res=dbo.insert(name,email,password)
      if res:
           return render_template('login.html',message="Registration Successfull!! Please proceed for Login")
      else :
        return render_template('register.html',message="Email Already Exist!!! Please try again with some other email")
    
@app.route('/perform_login',methods=['post'])
def perform_login():
    email=request.form.get('email')
    password=request.form.get('password')
    res=dbo.search(email,password)
    if res:
        return redirect("/profile")
    else :
        return render_template('login.html',error="Email Doesnot Exist!!! Please enter correct emailx")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    ner_input=request.form.get('ner_input')
    return ner_input


app.run(debug=True)