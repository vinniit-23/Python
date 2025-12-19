"""Problem: Customize a coffee order:
 "Small", "Medium", or "Large" with an option for "Extra shot" of espresso."""

print("Enter cofee size small,medium and large")
coffee_size =input()
extra_shot=True
if extra_shot :
    coffee = coffee_size + " with extra shot"
else :
    coffee = coffee_size
print(coffee)