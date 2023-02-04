import datetime
from flask import Flask,redirect
app= Flask(__name__,static_url_path="/static")

@app.route("/")
def index():
  page=""
  f = open("template/home.html","r")
  page = f.read()
  f.close()
  return page
  
@app.route("/blog/home")# use this to redirect you to a home page
def home_redirect():
  return redirect("/home")
    
@app.route("/blog/bye")#use this to redirect you to the page
def bye_redirect():
  return redirect("/bye")


@app.route("/home")
def blog1():
  link1 ="/bye"
  link2="/"
  name = "Hello World"
  today = datetime.datetime.today()
  today = today.strftime("%m/%d/%Y, %H:%M:%S")#converts the datetime dataty to str
  notes = "Welcome to my first blog entry."
  page =""
  f=open("template/blog.html","r")
  page = f.read()
  f.close()
  page = page.replace("name",name)
  page = page.replace("time",today)
  page= page.replace("notes",notes)
  page= page.replace("link1",link1)
  page= page.replace("link2",link2)
  return page

@app.route("/bye")
def bye():
  link2 ="home"
  link1="/"
  name = "Bye World"
  today = datetime.datetime.today()
  today = today.strftime("%m/%d/%Y, %H:%M:%S")#converts the datetime datatype to string
  notes = "Goodbye i will see you in my next blog."
  page =""
  f=open("template/blog.html","r")
  page = f.read()
  f.close()
  page = page.replace("name",name)
  page = page.replace("time",today)
  page= page.replace("notes",notes)
  page= page.replace("link1",link1)
  page= page.replace("link2",link2)
  return page

app.run(host="0.0.0.0",port=81)