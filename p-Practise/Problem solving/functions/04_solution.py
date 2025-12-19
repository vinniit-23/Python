"""Problem: Create a function 
that returns both the area and circumference of a circle given its radius.
"""
import math
def circle(radius):
    area = math.pi*radius**2
    circumference = math.pi*2*radius
    return area,circumference

print("enter radius of circle")
radius = int(input())

a,c=circle(radius)

print("Area",a,"circumference",c)

   