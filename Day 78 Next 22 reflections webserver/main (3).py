from flask import Flask
import datetime

url = {"78":{"link":"https://replit.com/@ValenciaFaith/Day78100Days#main.py",'reflection':"today was was not quite trilling but i had to push my self to code. Css is no fun",'prev':'/',"next":"/79"},
       
       "79":{"link":'https://replit.com/@ValenciaFaith/Day79100Days#index.html',"reflection":"learned how to create forms in html which is the only real way to communicate with the webserver","prev":'/78',"next":"/"},
      
       "80":{"link":'https://replit.com/@ValenciaFaith/Day80100Days#main.py',"reflection":"Built the webserver of the forms which was created in day 79 it was challenging but very exciting to see how you can make an interactive form","prev":'/79',"next":"/"}
       
       "81":{"link":'https://replit.com/@ValenciaFaith/Day81100Days#main.py',"reflection":"Project day!!. Today i built The lengendary I am not a robot program.it was quite interesting building it. Atleast i was able to understand how the backend works.","prev":'/80',"next":"/"}
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
