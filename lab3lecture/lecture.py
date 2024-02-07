#1
'''
def calculate_factorial(x):
    if x>1:
        res=x*calculate_factorial(x-1)
    else:
        res=1
    return(res)

print(calculate_factorial(4))
'''

#2
'''
def reverse_string(x):
    print(x[::-1])

reverse_string("qwerty")
'''

#3
'''
def get_max(a,b,c):
    print(a) if a>b and a>c else print(c) if c>a and c>b else print(b)

get_max(11,9,6)
'''

#4
'''
def is_even(a):
    print(a%2==0)

is_even(4)
'''

#5
'''
def prime(n): 
    if n <= 0: 
        return "Not defined" 
    elif n == 1: 
        return "Not prime" 
    for i in range(2, n): 
        if n%i == 0: 
            return "not prime" 
    return "prime" 
 
 
 
def list_prime(lst): 
    lst=list(lst.split())
    prime_list =[ ] 
    for i in lst: 
        x = prime(int(i)) 
        if x == "prime": 
            prime_list.append(i) 
    return prime_list 
	 
print(list_prime("1 2 3 4 5 6 7 8 79")) 
'''
#6
'''
def find_common_elements(x, y):
    x=set(x)
    y=set(y)
    z= x.intersection(y)
    print(z)

find_common_elements([1,2,8,5,6],[1,6,8,4,7])
'''

#7
'''
def word_frequency(x):
    a=dict()
    x=x.split()
    for i in x:
        z=x.count(i)
        a[i]=z

    print(a)

word_frequency("as as as ty ty gh")
'''

#8
'''
def recursive(x):
    if x>2:
        res=recursive(x-1)+recursive(x-2)
    else:
        res=1
    return (res)

print(recursive(3))
'''

#9
'''
def average(x, y, z):
    s=0
    n=0
    for i in range(y, z+1):
        s+=x[i-1]
        n+=1
    return float(s/n)
print(average([5,8,4,7,9,2,3,4],3,8))
'''

#10
'''import math
class My_shape:
    def __init__(self, color="white", is_filled=True):
        self.color=color
        self.is_filled=is_filled
    
    def __str__(self):
        return f"color is {self.color} area is self.is_filled" 
    
    def myArea(self):
        return 0
    
class Rectangle(My_shape):
    def __init__(self, color="white", is_filled=True, x_top_left=0, y_top_left=0, length=10, width=6 ):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}, Top Left: ({self.x_top_left}, {self.y_top_left}), Length: {self.length}, Width: {self.width}"

class Circle(My_shape):
    def __init__(self, color="white", is_filled=True, x_center=0, y_center=0, radius=5 ):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}, Center: ({self.x_center}, {self.y_center}), Radius: {self.radius}"
    
    
def ch():
 color=input("color")
 is_filled=input("Filled?")
 x_top_left=float(input("x left"))
 y_top_left=float(input("y left"))
 length=float(input("lenght"))
 width=float(input("width"))
 return Rectangle(color, is_filled, x_top_left, y_top_left, length, width)
 

print(ch())
print(Rectangle().getArea())
print(Circle().getArea())'''