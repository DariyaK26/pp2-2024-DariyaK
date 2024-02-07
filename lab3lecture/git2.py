#1
'''
def gr(x):
    oun=28.3495231*x
    print(oun)
gr(2)

#2
def F(x):
    C=(5/9)*(x-32)
    print(C)
F(2)

#3
def sol(h, l):
    r=(l-2*h)/2
    c=h-r
    print(c, r)

sol(35, 94)
    
#4
#in lecture

#5
from itertools import permutations

def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))

# Test the function
user_input = input("Enter a string: ")
print_permutations(user_input)

#6
def re(x):
    x=list(x.split())
    print(x[::-1])

re("as dg we sd")

#7
def has_33(nums):
    for i in range ( len(nums)-1):
        if nums[i]==3 and nums[i+1]==3:
            return True
    return False

print (has_33([1, 3, 3]) )
print(has_33([1, 3, 1, 3]) )
print(has_33([3, 1, 3]) )

#9
import math

def s(r):
    if r<0:
        return 0
    v=(4/3)*math.pi*(r**3)
    return v
print(s(5))

#10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


input_list = [1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
print("Original list:", input_list)
print("List with unique elements:", unique_elements(input_list))

#11

def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
'''
#12
def h(x):
    for i in x:
        print('*' * i)

h([2,5])


