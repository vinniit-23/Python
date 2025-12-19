"""Problem: Recommend a type of pet food based on the pet's species and age. 
(e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)."""

print("Enter pet species and age : ")
species = input()
age = int(input())
if species == "dog":
    if age < 2 :
        print("puppy food")
    else :
        print(" Dog food ")
elif species == "cat":
    if age > 5 :
        print("senior cat food")
    else :
        print("baby cat food")