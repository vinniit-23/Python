"""Problem: Determine if a fruit is ripe, overripe, or unripe based on its
 color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)"""

fruit = "Banana"
print("Enter banana color")
color = input()
if color == "green" :
    print("Unripe")
elif color == "yellow":
    print("Ripe")
elif color == "brown":
    print("over ripe")
else:
    print("Invalid input")