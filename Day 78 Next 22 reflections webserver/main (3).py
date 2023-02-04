from flask import Flask
import datetime

url = {"78":{"link":"https://replit.com/@ValenciaFaith/Day78100Days#main.py",'reflection':"today was was not quite trilling but i had to push my self to code. Css is no fun",'prev':'/',"next":"/79"},
       
       "79":{"link":'/79',"reflection":'Learned how to create templates in html which to be honest i dont know how i felt doing that.',"prev":'/78',"next":"/"}
      
      }

app=Flask(__name__,static_url_path="/static")

@app.route('/')
def index():
  time= datetime.datetime.today()
  time = time.strftime("%m/%d/%Y, %H:%M:%S")
  page = ""
  f = open("template/index.html","r")
  page = f.read()
  f.close()
  page = page.replace("time",time)
  return page

@app.route("/<pagenumber>")
def seventy_8(pagenumber):
  time= datetime.datetime.today()
  time = time.strftime("%m/%d/%Y, %H:%M:%S")
  link = url[pagenumber]["link"]
  reflection = url[pagenumber]['reflection']
  page = ""
  f = open("template/reflecion.html","r")
  page = f.read()
  f.close()
  page = page.replace("time",time)
  page = page.replace('number',pagenumber)
  page = page.replace("{link}",link)
  page = page.replace("reflections",reflection)
  
  page=page.replace('plink',url[pagenumber]['prev'])
  page=page.replace('nlink',url[pagenumber]['next'])
  return page
app.run(host="0.0.0.0",port=81)
