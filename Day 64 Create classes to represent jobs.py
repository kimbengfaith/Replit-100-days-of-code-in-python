# Day 64 challenge: Create classes to represent jobs
class job:
  def __init__(self,name,salary,hours_worked):
    self.name = name
    self.salary = salary
    self.hours = hours_worked

  def preetyprint(self):
    print(f"Job type: {self.name:^5} \nSalary: {self.salary:^5} \nHours worked: {self.hours:^5}")

# doctor subclass
class doctor(job):
  def __init__(self,salary,hoursworked,speciality,yof): # yof = years of experience
    self.name = "Doctor"
    self.salary = salary
    self.hoursworked = hoursworked
    self.speciality = speciality
    self.yof = yof

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursworked:>10}")
    print(f"{self.yof:<10} {self.speciality:>21}")
    
# Teacher class    
class teacher(job):
  def __init__(self,salary,hoursworked,subject,position):
    self.name = "Teacher"
    self.salary = salary
    self.hoursworked = hoursworked
    self.subject = subject
    self.position = position

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursworked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")

lawyer = job("lawyer","$ Squillions",60)
print(lawyer.preetyprint())
print()

teacher = teacher("Nowhere near enough","all of them","Computer science","Classroom Teacher")
print(teacher.print())
print()

doctor = doctor("$ Doing very nicely thank you",50,"Pediatric Consultant",7)
print(doctor.print())