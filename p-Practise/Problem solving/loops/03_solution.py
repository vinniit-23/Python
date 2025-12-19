"""Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
"""
print("Enter number to print the multiplication table")
num = int(input())

for i in range(1,11):
    if num == 5:
        continue
    multiplication = num * i
    print("%d x %d = %d" % (num, i, multiplication)) 
     
        