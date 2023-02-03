from flask import Flask
import datetime
app= Flask(__name__,static_url_path="/static")
@app.route('/')
def index():
  today= datetime.datetime.today()
  page = f"""
  <html>
   <body>
    <h2>{today}</h2>
    <p><a href="/portfolio">My portfolio</a></p>
    <p><a href="/linktree">My linktree</a></p>
   </body>
  </html>
  """
  return page
  
@ app.route('/portfolio')
def portfolio():
  page="""
  <html>
  
   <head>
     <title>My Portfolio</title>
     <link href="static/css/portfolio.css"" rel="stylesheet" type="text/css" />
   </head>
  
   <body>
     
     <h1>Kimbeng Faith Antia Portfolio</h1>
     <a class="f" href="https://github.com/kimbengfaith">Github</a>
     <p class="faith1"> Hi am called kimbeng faith and these are some of my best and challenging 100 days of replit's python projects.Click on the images to see the various codes.</p>
     
     <h2>Day 56: Music Streaming service.</h2>
     
     <p>Today, we were to use the csv library and the file management in python to create a Music Streaming service. The programe had to do the following</p>
     <ol>
       <li>Read in the data</li>
       <li>Create a folder to Catergorize each song by their artist like </li>
     </ol>
     <p>Click on the image to get access to the direct repl</p>
     <a href="https://replit.com/@ValenciaFaith/Day56100Days#main.py"><img src="static/images/day56.png" width = 50%></a>
     
     <h2>Day 53: The Inventory Video Game</h2>
     
     <p>Todays challeng we had to create an inventory game system. we need to have a menu the Adds, Removes, and views an item using autoload and autosave.</p>
     
     <ul>
       <li>Adding an item save a file using capitalize mode.</li>
       <li>Removing an item deletes it from the file</li>
       <li>View should output an item and tell you howmany of those items are there.</li>
     </ul>
     <a href="https://replit.com/@ValenciaFaith/Day56100Days#main.py"><img src="static/images/day53.png" width = 50%></a>
     
     
      <h2>Day 72: Advanced Secret Diary</h2> 
     
      <p>This challeng is about creating your own secret diary and converting your passwords to hashes and salts to prevent Hackers from geting the password easily.The Diary does the following </p>
     
       <ul>
         <li>The first time you run the programe it will prompt you to create your username and password.</li>
         <li>The next time you run the program it will ask you to input your correct username and password.if one is incoreect you wont gain any access to your diary.</li>
      
       </ul>
     
       <p>The diary can both Add and View items</p>
     
       <ul>
         <li>If add is choosen its will ask you for the item then add it to your diary but,</li>
         <li>if view is choosen then it will view the most recent Added item and the time it was added.The diary will then ask you if you want to see the next time or move ahead.</li>
       </ul>
     
       <a href = "https://replit.com/@ValenciaFaith/Day72100Days#main.py"><img src="static/images/day72.png" width = 50%></a>

       <h2>Day 47: Top Trumpers</h2>
       <p>Top trumpers is a game where you can pick a catergory of thing like "the most beautiful girls in class and compare them based on some statistics.The statistics could be on the following."</p>
       <ul>
         <li>Their intelligence level</li>
         <li>Coding skills</li>
         <li>Dressing skills etc.</li>
       </ul>
     
       <p>The code is written in such a way that only 2 playes can actualy play.That is yourself and the computer.For more, click the picture below get the instructions and the code,</p>
       <a href = "https://replit.com/@ValenciaFaith/Day47100Days#main.py"><img src = "static/images/day47.png" width = 50%></a>
     
       <h2>Day 28: Automated Game Battle System</h2>
     
       <p>This is the battle for your life game where two of your favourite characters either in cartoons or in movies will be battling against one another.</p>
       <p>The instructions is as follows...</p>
     
       <ul>
         <li>The 2 characters will need to roll a 6 sided dice each.</li>
         <li>If the first chaarcter wins his health remains thesame and the health of the second character will be subtracted by the difference in their strenghts.</li>
         <li>If they both have thesame dice roll they are both moving on to the next round.</li>
         <li>The status of both characters will be pasted after each round.</li>
       </ul>
      <a href="https://replit.com/@ValenciaFaith/day28100-days-of-code-Automated-Game-Battle-System#main.py"><img src="static/images/day28.png" width=50%></a>
      <p><a href="/linktree">My linktree</a></p>
   </body>


</html>
  """
  return page

@app.route("/linktree")
def linktree():
  page="""
  <html>
  <head>
    <title>My link tree</title>
    <link rel="stylesheet" href="static/css/linktree.css"">
  
  </head>
  <body>
     <img src = "static/images/myimage.jpg" width = 40% height = 40%>
     <h1>Kimbeng Faith Antia Va Ndze</h1>
     <p>Python developer/Data scientist/MachineLearning/Cybersecurity</p>
     <h3 class="s">Socials</h3>
     <ul>
       <li><a href="https://github.com/kimbengfaith">Github</a></li>
       <li><a href="https://twitter.com/Valencia20033">Twitter</a></li>
       <li><a href="https://www.linkedin.com/in/kimbeng-faith-antia-0497b7204/">linkedin</a></li>
     </ul>
     <h3 class="p">Projects</h3>
     <ul>
       <li><a href="https://replit.com/@ValenciaFaith/Day56100Days#main.py">Music Streaming service</a></li>
       <li>
         <a href = "https://replit.com/@ValenciaFaith/Day53100Days#main.py">The Inventory Video Game</a>
       </li>
       <li>
         <a href = "https://replit.com/@ValenciaFaith/Day72100Days#main.py">Advance Secret Diary</a>
       </li>
       <li>
         <a href = "https://replit.com/@ValenciaFaith/Day47100Days#main.py">Top Trumpers</a>
       </li>
       <li>
         <a href="https://replit.com/@ValenciaFaith/day28100-days-of-code-Automated-Game-Battle-System#main.py">Automated Game Battle System</a>
       </li>
     </ul>
     
     <img class="gl" src ="static/images/google.png" width = 20% height="10%"

     <p><a href="/portfolio">My portfolio</a></p>



    
  </body>
  
  </html>
  """
  return page

app.run(host="0.0.0.0",port=81)