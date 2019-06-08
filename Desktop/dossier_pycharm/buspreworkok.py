# variables
x = 21
y = 6
i = 0

bus_stop = (x, y)
stops = [(x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3), (x + 4, y + 4)]

# 1. Calculate the number of stops.

print(len(stops))

len(stops)
while i < len(stops):
    print(stops[i])
    i += 1

# 2. Assign a variable a list whose elements are the number of passengers in each stop:

number_passenger = [(x + 1 - (y + 1)), (x + 2 - (y + 2)), (x + 3 - (y + 3)), (x + 4 - (y + 4))]
print(number_passenger)

# Each item depends on the previous item in the list + in - out.

number_passenger = [(x + 1 - (y + 1)) + (x + 2 - (y + 2)) + (x + 3 - (y + 3)) + (x + 4 - (y + 4))]
print(number_passenger)

# 3. Find the maximum occupation of the bus.
number_passenger = [(x + 1 - (y + 1)) + (x + 2 - (y + 2)) + (x + 3 - (y + 3)) + (x + 4 - (y + 4))]
max = 0
i = 0
while i < len(number_passenger):
    if number_passenger[i] >= max:
        max = number_passenger[i]
    i = i + 1
print(max)

# calcul minimum
min = 0
i = 0
while i > len(number_passenger):
    if number_passenger[i] <= min:
        min = number_passenger[i]
    i = i + 1
print(min)


# 4. Calculate the average occupation. And the standard deviation.
# Python program to get average of a list
# Using mean()

# importing mean()
from statistics import mean


def Average(lst):
    return mean(lst)


# Driver Code
lst = [(x + 1 - (y + 1)) + (x + 2 - (y + 2)) + (x + 3 - (y + 3)) + (x + 4 - (y + 4))]
average = Average(lst)

# Printing average of the list
print("Average of the list =", round(average, 2))

import statistics
statistics.pstdev([(x + 1 - (y + 1)) + (x + 2 - (y + 2)) + (x + 3 - (y + 3)) + (x + 4 - (y + 4))])


import numpy as np
np.std([(x + 1 - (y + 1)) + (x + 2 - (y + 2)) + (x + 3 - (y + 3)) + (x + 4 - (y + 4))])
