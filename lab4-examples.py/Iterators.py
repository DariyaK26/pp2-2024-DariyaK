'''#1
mytuple =('apple', 'banana', 'cherry')
it=iter(mytuple)

print(next(it))
print(next(it))
print(next(it))

#2
mystr='banana'
it=iter(mystr)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#3
mytuple =('apple', 'banana', 'cherry')

for x in mytuple:
    print(x)

#4
mystr='banana'

for x in mystr:
    print(x)'''

#5
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#6
class Nums:
  def __iter__(self):
    self.a=1
    return self
  
  def __next__(self):
    if self.a<=20:
      x=self.a
      self.a+=1
      return x
    else:
      raise StopIteration
    
clas=Nums()
itr=iter(clas)

for x in itr:
  print(x)
