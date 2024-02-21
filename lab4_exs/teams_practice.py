#1

#import math
#x=180
#print(math.radians(x))

#2
#base_1 = 5
#base_2 = 6
#height = float(input())
#base_1 = float(input())
#base_2 = float(input())
#area = ((base_1 + base_2) / 2) * height
#print("Area is:", area)

#3
#num=float(input())
#length=float(input())
#area=(num*length*(length/(2*math.tan(math.radians(180/num)))))/2
#print(math.floor(area))

#Date
#1
'''
import datetime
#print(datetime.date.today()-datetime.timedelta(5))


#2
x=datetime.date.today()
print(x.strftime("%A"))
y=x-datetime.timedelta(1)
print(y.strftime("%a"))
z=x+datetime.timedelta(1)
print(z.strftime("%A"))

#3
x=datetime.datetime.today().replace(microsecond=0)
print(x)

#4
def sec(t2, t1):
    datetime.timedelta=t2-t1
    return datetime.timedelta.days*24*3600+datetime.timedelta.seconds

tm1=datetime.datetime.strptime('2020-01-01 15:35:08', "%Y-%m-%d %H:%M:%S")
tm2=datetime.datetime.now()
print("\n%d second" %(sec(tm2,tm1)))
'''
#generator
#1
#def w(n):
#    for i in range(n):
#        yield (i**2)
#
#
#for x in w(10):
#    print (x)


#2

#def even(n):
#    for i in range(0, n):
#        if i%2==0:
#            yield i
#
#n=int(input())
#for x in even(n):
#    print(x)

#3
#n = int(input())
#divBy34 = [i for i in range(0, n) if (i % 3 == 0 and i%4==0)]
#print(divBy34)
#
#def divChecker(n):
#    for i in range(n):
#        if (i % 3 == 0 and i%4==0):
#            value = True
#        else:
#            value = False
#        print(i, value)
#
#divChecker(n)

#4
#def sqw(a, b):
#    for i in range(a, b):
#        yield(i**2)
#a, b= int(input()), int(input())
#for x in sqw(a,b):
#    print(x)

#5
def down(n):
    for i in range (n, -1, -1):
        yield i
n=int(input())
for x in down(n):
    print (x)