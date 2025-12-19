"""Problem: Write a function to calculate and return the square of a number.
"""
def power(num_1,num_2):
     return num_1 ** num_2 

print("enter the base number")
num_1 = int(input())
print("enter the power number")
num_2 = int(input())

num_3=power(num_1,num_2)
print("your answer is",num_3)


