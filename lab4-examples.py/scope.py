#1
def myfunc():
  x = 300
  print(x)

myfunc()

#2
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() 

#3
x=300
def func():
  print(x)

func()
print(x)

#4
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


#5
def myfunc():
  global x
  x = 300

myfunc()

print(x)

#6
def myfunc():
  global x
  x = 300

myfunc()

print(x)