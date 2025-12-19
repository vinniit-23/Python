"""Problem: Determine if a year is a 
leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400)."""

print("Enter year to find if it leap or not", end= " ")
year = int(input())
if (year % 4 == 0) or (year % 400 !=0 ):
    if (year % 400 == 0) :
        print("Given year is Leap year")
else :
    print(" the given year is not leap year")
