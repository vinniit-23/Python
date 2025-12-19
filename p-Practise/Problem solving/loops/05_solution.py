"""Problem: Given a string, find the first non-repeated character."""
print("Enter the String")
input_str = input()
for char in input_str:
    if input_str.count(char) == 1:
        print("repeated character is : ", char)
        break
