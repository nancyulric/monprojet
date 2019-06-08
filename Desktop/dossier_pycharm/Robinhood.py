# Variables

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

# 2. Calculate how many arrows have fallen in each quadrant.

for i, elt in points:
    if i > 0 and elt >= 0:
        
         print("The arrow is in the quadrant 1.")

    elif i <= 0 and elt > 0:
        print(i, elt)
        print("The arrow is in the quadrant 2.")

    elif i < 0 and elt < 0:
        print(i, elt)
        print("The arrow is in the quadrant 3.")

    elif i >= 0 and elt < 0:
        print(i, elt)
        print("The arrow is in the quadrant 4.")
    else:
        print("The arrow is out of the quadrant.")

# 3. Find the point closest to the center. Calculate its distance to the center
# Defining a function that calculates the distance to the center can help.

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
          (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
          (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

dupe = set(points)
print(dupe)

dupe = [(-4, 5), (4, 7), (3, 2), (4, 5), (-1, 3), (5, 7), (9, 9), (3, -2), (-5, 7),
        (-3, 2), (0, -2), (-4, -5), (2, 2), (-8, -9), (1, -3), (-4, 7), (0, 2)]

dupe.sort()
print(dupe)
dupe = [(-8, -9), (-5, 7), (-4, -5), (-4, 5), (-4, 7), (-3, 2),
        (-1, 3), (0, -2), (0, 2), (1, -3),
        (2, 2), (3, -2), (3, 2), (4, 5), (4, 7), (5, 7), (9, 9)]

import math


p1 = [0, 0]
p2 = [0, -2]
distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
print(distance)
print(" The point (0, -2) is at 2.0 from the center")


p1 = [0, 0]
p2 = [-0, 2]
distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
print(distance)
print(" The point (-0, 2) is at 2.0 from the center")
print("The points closest to the center are (-0, 2) and (0, -2).")

# 4. If the target has a radius of 9, calculate the number of arrows that
# must be picked up in the forest.

for i, elt in points:
    if i <= 9 and elt <= 9:
        print(i, elt)
        print("The arrow is on the target.")
    else:
        print("We will pick up the arrow.")
