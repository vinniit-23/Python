""""Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)."""
print("enter marks between 0 to 100")
marks = int (input())
if marks > 100:
    print("invalid marks")
    exit()
elif marks <= 100 and marks >= 90:
    print("your grade is A")
elif marks<= 89 and marks >= 80:
    print("your grade is B")
elif marks<= 79 and marks >= 70:
    print("your grade is C")
elif marks<= 69 and marks >= 60:
    print("your grade is D")
else :
    print("your grade is F")

