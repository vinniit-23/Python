"""Problem: Choose a mode of transportation based on the distance
 (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
"""
print("enter distance in Km")
distance = int(input())
if distance < 3 :
    print("Walk")
elif distance > 3 and distance < 15 :
    print("use bike")
elif distance > 15:
    print("use car")