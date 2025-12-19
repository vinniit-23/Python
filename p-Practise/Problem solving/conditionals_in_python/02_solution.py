"""Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
"""
print("Enter your age :", end=" ")
age = int(input())
print("Enter day :", end= " ")
day = input()
if  day == "wednesday":
    if age > 18 :
        price = 12 -2
        print ("ticket price is $", price)
    else :
        price = 8 -2
        print("ticket price is $",price)
else :
        if age > 18 :
         price = 12 
         print ("ticket price is $", price)
        else :
         price = 8 
         print("ticket price is $",price)