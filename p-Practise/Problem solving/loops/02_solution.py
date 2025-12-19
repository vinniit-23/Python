"""Problem: Calculate the sum of even numbers up to a given number n.
"""
print("enter number of numbers: ",end="")
numbers = int(input())
count_even_number = 0
for i in range(0,numbers):
    if i % 2==0:
        count_even_number += 1
print("number of even numbers",count_even_number)