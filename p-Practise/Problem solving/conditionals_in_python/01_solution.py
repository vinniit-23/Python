# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
print("Enter your age:", end=" ")
age = int(input())
if age < 13:
    print("child")
elif age <20:
    print("teenager")
elif age < 60:
    print("adult")
else : 
    print("senior")
     
