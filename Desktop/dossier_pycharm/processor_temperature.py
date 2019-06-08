# assign a variable to the list of temperatures

temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64,
                  70, 76, 80, 69, 80, 83, 68, 79,
                  61, 53, 50, 49, 53, 48, 45, 39]

# 1. Calculate the minimum of the list and print the value using print()
print(min(temperatures_C))

# 2. Calculate the maximum of the list and print the value using print()
print(max(temperatures_C))

# 3. Items in the list that are greater than 70ºC and print the result
for i in temperatures_C:
    if i > 70:
        print(i)


# 4. Calculate the mean temperature throughout the day and print the result
def moyenne(temperatures_C):
    return sum(temperatures_C) / len(temperatures_C)


print(moyenne(temperatures_C))

# 5.1 Solve the fault in the sensor by estimating a value
# 5.2 Update of the estimated value at 03:00 on the list
temperatures_C[3] = 59
print(temperatures_C)

# Bonus: convert the list of ºC to ºFarenheit
# Farenheit = Celsius * 1,8 + 32

for celsius in temperatures_C:
    print((celsius * 1.8) + 32)

temperatures_F = (91.4, 150.8, 149.0, 138.2, 138.2,
                  140.0, 143.6, 147.2, 158.0, 168.8,
                  176.0, 156.2, 176.0, 181.4, 154.4,
                  174.2, 141.8, 127.4, 122.0, 120.2,
                  127.4, 118.4, 113.0, 102.2)

# Take the decision
# Print True or False depending on whether you would change the cooling system or not
# more than 4 hours with temperatures greater than or equal to 70ºC
# some temperature higher than 80ºC
# average was higher than 65ºC throughout the day If any of these three is met, the cooling system must be changed.


temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64,
                  70, 76, 80, 69, 80, 83, 68, 79,
                  61, 53, 50, 49, 53, 48, 45, 39]

for i in range(len(temperatures_C)):
    if temperatures_C[i] >= 70 and len(temperatures_C) > 4:
        print("temperature = {}".format(temperatures_C[i]), "true,we change the cooling system.")
        if temperatures_C[i] > 80 or moyenne(temperatures_C[i]) > 65:
            print("temperature = {}".format(temperatures_C[i]), "true,we change the cooling system.")
        else:
            print("temperature = {}".format(temperatures_C[i]), "false,we don't need to change the cooling system.")

# Future improvements
# 1. We want the hours (not the temperatures) whose temperature exceeds 70ºC
# 2. Condition that those hours are more than 4 consecutive and consecutive, not simply the sum of the whole set. Is this condition met?

for index, temperature in enumerate(temperatures_C):
    if temperature >= 70:
        print("At {} hours the temperature was {} °C.".format(index, temperature))


# 3. Average of each of the lists (ºC and ºF). How they relate?
def moyenne(temperatures_F):
    return sum(temperatures_F) / len(temperatures_F)


print(moyenne(temperatures_F))
print(moyenne(temperatures_C))

# Convertir les données modifient les valeurs mais ne modifient pas les constats. Le traitement des données reste le même.

# 4. Standard deviation of each of the lists. How they relate?

# Python code to demonstrate use of xbar
# parameter while using stdev() function

# Importing statistics module
import statistics

# creating a temperatures_F (sample)

temperatures_F = (91.4, 150.8, 149.0, 138.2, 138.2,
                  140.0, 143.6, 147.2, 158.0, 168.8,
                  176.0, 156.2, 176.0, 181.4, 154.4,
                  174.2, 141.8, 127.4, 122.0, 120.2,
                  127.4, 118.4, 113.0, 102.2)
# calculating the mean of sample set
m = statistics.mean(temperatures_F)

# xbar is nothing but stores
# the mean of the sample set

# calculating the variance of sample set
print("Standard Deviation of temperatures_F set is % s"
      % (statistics.stdev(temperatures_F, xbar=m)))

# calculating the mean of sample set temperatures_C
m = statistics.mean(temperatures_C)

# xbar is nothing but stores
# the mean of the sample set

# calculating the variance of sample set
print("Standard Deviation of temperatures_C set is % s"
      % (statistics.stdev(temperatures_C, xbar=m)))

# Convertir les données modifient les valeurs mais ne modifient pas les constats. Le traitement des données reste le même.
