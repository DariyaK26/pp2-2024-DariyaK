'''#1
t=int(input())
s=[]
for i in range(t):
    a=int(input())
    s.append(a)
l=1
for i in s:
    l*=i

print(l)

#2
p=input()
L=0
U=0
for i in p:
    if i.isupper():
        U+=1
    elif i.islower():
        L+=1

print(L, U) 

#3
p=input()
if (p==p[::-1]):
    print('yes')
else:
    print("no")

#4
from time import sleep
import math
def delay(fn, ms, *args):
    sleep(ms / 1000)
    return fn(*args)
z=int(input())
y=int(input())
print(delay(lambda z: math.sqrt(z),y,z))
'''
#5
p=('skdldf',  "skfsl", 0, True)
print( all(p))

