

import os
os.getcwd()


os.chdir('/Users/Nancy/Desktop')
os.getcwd()
        
data = []

with open(r"C:\Users\Nancy\Desktop\weight_height.csv", "r") as f:
    lines = f.readlines()
    for line in lines:
        data.append(line.split()[0].split(","))





















