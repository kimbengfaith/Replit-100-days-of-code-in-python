from flask import Flask,request

app=Flask(__name__,static_url_path="/static")

#dictionary to store your 3 valid combination
details={'faith':{"email":"valencia@716.gmail.com","password":"valen123#"},
        'divine':{"email":"a@gamil.com",'password':"123456"},
        'bless':{'email':"b@gamil.com","password":'789012'}
        }

key=details.keys()


@app.route("/")
def index():
  page=""
  f=open("index/form.html","r")
  page=f.read()
  f.close()
  return page

@app.route("/form",methods=['POST'])
def process():
  form=request.form
  try:
    if form['username'] in key and form['password']==details[form['username']]['password']:
      
      page= "You are logged in "
    else:
      page="Username,Email or password incorrect"
  except:
    page="Username,Email or password incorrect"

  return page
    
    
    

app.run(host='0.0.0.0',port=81)
