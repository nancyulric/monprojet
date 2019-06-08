# variables
x = 21
y = 6
i = 0

a = 25
b = 18
c = 6
d = 13
e = 9
f = 3
g = 16
h = 8

bus_stop = (x, y)
stops = [(x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3), (x + 4, y + 4)]

# 1. Calculate the number of stops.

print(len(stops))

len(stops)
while i < len(stops):
    print(stops[i])
    i += 1

# 2. Assign a variable a list whose elements are the number of passengers in each stop:

number_passenger = (a - b) + (c - d) + (e - f) + (g - h)
print(number_passenger)
number_passenger_list = [(a - b), (c - d), (e - f), (g - h)]
# Each item depends on the previous item in the list + in - out.

# 3. Find the maximum occupation of the bus.
print(max(number_passenger_list))