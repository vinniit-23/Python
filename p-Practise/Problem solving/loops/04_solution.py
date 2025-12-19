"""Problem: Reverse a string using a loop.
"""
print("Enter the string")
input_str = input()
reversed_str = ""
for i in input_str:
    reversed_str = i + reversed_str
    #print(reversed_str)
print(reversed_str)
 