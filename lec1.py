# Lab 1 Task 1

"""
Define a function MaxOfThree() that takes three numbers as arguments and
returns the largest of them (Use If, elif and else). For example, MaxOfThree(1, 2, 3)
should return 3.
"""
def maxOfThree(x,y,z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z
    else:
        return 0


x = 1
y = 2
z = 3
print("Max number is: " + str(maxOfThree(x,y,z)))


# Lab 1 Task 2
"""
Define a function MySum() and a function MyMultiply() that sums and multiplies
(respectively) all the numbers in a list of numbers (Use for). For example, s
MySum([1, 2, 3, 4]) should return 10, and MyMultiply([1, 2, 3, 4]) should return 24.
"""

my_list = [1,2,3,4]


def MySum(l):
    sum_res = 0
    for i in l:
        sum_res += i
    return sum_res


def MyMultiply(l):
    mult_res = 1
    for i in l:
        mult_res *= i
    return mult_res


print("MySum is: " + str(MySum(my_list)))
print("MyMultiply is:" + str(MyMultiply(my_list)))


# Lab 1 Task 3
"""
Define a function MyMean() that receives an unknown amount of input values
from a user and returns the mean value of all the input values (Use while). For
example: if the user provides [1, 2, 3, 4], the MyMean(), should return 2.5
"""

def MyMean(m):
    i = 0
    mean = 0
    while i < len(m):
        mean += m[i]
        i += 1
    return mean/len(m)


received_num = []
try:
    inp = input("Enter a number: ")
except SyntaxError:
    inp = None

while inp:
    received_num.append(float(inp))
    try:
        inp = input("Enter a number: ")
    except SyntaxError:
        inp = None

print("Mean of numbers is: " + str(MyMean(received_num)))

# Lab 1 Task 4
"""
Define a function MyStars() that takes a list of integers and prints a string of stars
which has the length of a value of an integer to the screen. For example, MyStars([3,
9, 7]) should print the following:
***
*********
*******
"""
def MyStars(lst):
    i = 0
    for i in lst:
        print("*"*i)


star_list = []
inp4 = 1
while inp4:
    try:
        inp4 = input("Enter a number: ")
    except SyntaxError:
        inp4 = None
        break
    star_list.append(inp4)

MyStars(star_list)
