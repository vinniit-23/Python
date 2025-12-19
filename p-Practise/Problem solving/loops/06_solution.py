"""Problem: Compute the factorial of a number using a while loop."""
print("enter the number which you want to find factorial")
num = int(input())
factorial =1
while num>0:
    factorial *=num
    num -=1
    
    
print("factorial of given number is : ",factorial)