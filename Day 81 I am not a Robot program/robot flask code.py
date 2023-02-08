from flask import Flask,request

app= Flask(__name__)

#must include the main page
@app.route("/")
def index():
  #page = ""
  f=open("index/robot.html","r")
  page= f.read()
  f.close()
  return page

#checks if you are a robot
@app.route("/robot",methods=['POST'])
def robot():
  form = request.form
  if form['answer'].lower()=='yes' and form['food'].lower()=="human food" and form['infinity'].lower()== "infinity":
    page="Hi there fellow human"
  else:
    page="You are a robot"
  return page
  

app.run(host="0.0.0.0",port="81")
