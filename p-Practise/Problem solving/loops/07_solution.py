"""Problem: Keep asking the user for input until they enter a number between 1 and 10."""
while True:
    print("Enter number between 1 to 10")
    input_str = int(input())
    if 1<= input_str <=10:
        print("you are in ")
        break
    else :
        print("invalid input")