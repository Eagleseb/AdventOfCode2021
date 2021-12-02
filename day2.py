import numpy as np

with open('resources/day2') as file:
    movements = np.array([line.split() for line in file.readlines()])

count = np.int32(movements[:, 1])
action = movements[:, 0]
# step 1
x = np.sum(count[action == "forward"])
y = np.sum(count[action == "down"]) - np.sum(count[action == "up"])
print(x * y)

# step 2
aim = np.cumsum(count * [action == "down"] - count * [action == "up"])
x = np.sum(count[action == "forward"])
y = np.sum((count * aim)[action == "forward"])
print(x * y)
