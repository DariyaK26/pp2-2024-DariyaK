#1
'''
class stringg:
    def __init__(self):
        self.name=""

    def getString(self):
        self.name=input()

    def printString(self):
        print(self.name.upper())

ds=stringg()
ds.getString()
ds.printString()
'''
#2
'''
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length=length
    
    def area(self):
        return self.length**2
    
shape=Shape()
print(shape.area())
square=Square(5)
print(square.area())
'''

#3
'''
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle():
    def __init__(self, length, width):
        super().__init__()
        self.length=length
        self.width=width

    def area(self):
        return self.width*self.length
    
rec=Rectangle(8, 5)
print (rec.area())
'''

#4
'''
import math
class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        print(self.x, self.y)

    def move(self, nx, ny):
        self.x=nx
        self.y=ny

    def dist(self, other):
        dx=self.x-other.x
        dy=self.y-other.y
        dis=math.sqrt(dx**2+dy**2)
        return dis
    
point1 = Point(3, 4)
point2 = Point(6, 8)

point1.show()
point2.show()

print( point1.dist(point2))

point1.move(1, 2)
point1.show()
'''

#5
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} accepted. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} accepted. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")


account = BankAccount("John Doe", 1000)
print("Account owner:", account.owner)
print("Initial balance:", account.balance)

account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  

#6
#in lecture
