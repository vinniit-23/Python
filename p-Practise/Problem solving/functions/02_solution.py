"""Problem: Create a function that takes two numbers as parameters and returns their sum.
"""

def sum(num_1,num_2):
    return num_1+num_2

print("enter number one : ", end = " ") 
num_1=int(input())
print("enter number two",end = " ")
num_2=int(input())

print("addition of two number is %d"%(sum(num_1,num_2)))