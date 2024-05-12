from flask import Flask,render_template,request,redirect,session
from db import Database
import api

dbo=Database()

app=Flask(__name__)
app.secret_key = "super secret key" 

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
        session['logged_in']=1
        return redirect("/profile")
    else :
        return render_template('login.html',error="Email Doesnot Exist!!! Please enter correct emailx")

@app.route('/profile')
def profile():
    print(session['logged_in'])
    if session['logged_in']==1:
        return render_template('profile.html')
    else:
        return redirect("/")

@app.route('/ner')
def ner():
     if session['logged_in']==1:
        return render_template('ner.html')
     else:
        return redirect("/") 

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session['logged_in']==1:
        ner_input=request.form.get('ner_input')
        res=api.ner(ner_input)
        return render_template('ner.html',response=res)
    else:
        return redirect("/")
    
@app.route('/logout')
def perform_logout():
    session['logged_in']=0
    return redirect("/")
    

app.run(debug=True)