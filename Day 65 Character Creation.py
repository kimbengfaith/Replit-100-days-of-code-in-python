# Day 65 challenge": Character creation
class character:
  health =100
  magicpoints = 100
  def __init__(self,name):
    self.name = name
    

  def print(self):
    print(f"name: {self.name} \nhealth: {self.health} \nMagic points: {self.magicpoints}")

class player(character):
  def __init__(self,name,nol):  # nol = number of lives
    self.name = name
    self.nol = nol
  def print(self):
    print("Player")
    print(f"name: {self.name} \nhealth: {self.health} \nMagic points: {self.magicpoints} \nNumber of lives: {self.nol}")
    
  def isAlive(self):
    if self.nol > 0:
      print("Alive? ",end='')
      return True
    else:
      print("Alive? ",end='')
      return False
      
#char = character("Faith",100,100)
player = player("David",100)
print(player.print())
print(player.isAlive())
print()

class enemy(character):
  strength = 80
  def __init__(self,name,health,magicpoints,type,strength):
    self.name = name
    self.type = type
    
  def print(self):
    print(f"name: {self.name} \nhealth: {self.health} \nMagic points: {self.magicpoints} \ntype: {self.type} \nstrength: {self.strength}")

class orc(enemy):
  def __init__(self,name,speed):
    self.name = name
    self.type = "Orc"
    self.speed = speed
  def print(self):
    print(f"name: {self.name} \nhealth: {self.health} \nMagic points: {self.magicpoints} \ntype: {self.type} \nstrength: {self.strength} \nSpeed: {self.speed}")

class vampire(enemy):
  def __init__(self,name,day_night):
    self.type = "Vampire"
    self.name = name
    self.day_night = day_night

  def print(self):
    print(f"name: {self.name} \nhealth: {self.health} \nMagic points: {self.magicpoints} \ntype: {self.type} \nStrenght: {self.strength} \nDay or night: {self.day_night}")

susan = orc("susan","day")
print(susan.print())
print()
rishi = vampire("Rishi","day")
print(rishi.print())
    