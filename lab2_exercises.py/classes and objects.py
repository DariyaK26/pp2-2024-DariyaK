#1
class MyClass:
    x=5

#2
class MyClass:
    x=5
p1=MyClass()

#3
class MyClass:
    x=5

p1=MyClass()
print()

#4
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

#5
# class Student(Person):

#6
   
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

