# variables
i = 0
x = 5
y = 8
stops = ((x + 1, y - 1), (x + 2, y - 2), (x + 3, y - 3), (x + 4, y - 4))

# 1. Calculate the number of stops.

len(stops)
while i < len(stops):
    print(stops[i])
    i += 1

print(len(stops))

# 2. Assign a variable a list whose elements are the number of passengers in each stop:

stops = [(x + 1, y - 1), (x + 2, y - 2), (x + 3, y - 3), (x + 4, y - 4)]
number_passenger = 12, 5, 9, 15
stops.insert(0, 12)
stops.insert(2, 5)
stops.insert(4, 9)
stops.insert(6, 15)

print('Updated List:', stops)
Updated List: [12, (6, 7), 5, (7, 6), 9, (8, 5), 15, (9, 4)]


# Each item depends on the previous item in the list + in - out.

# 3. Find the maximum occupation of the bus.

# 4. Calculate the average occupation. And the standard deviation.
