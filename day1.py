import numpy as np

with open('resources/day1') as file:
    measurements = np.array([int(line) for line in file.readlines()])

# step 1
delta = measurements[1:] - measurements[:-1]
increases = np.sum(delta > 0)
print(increases)

# step 2
windowed_measurements = measurements[0:-2] + measurements[1:-1] + measurements[2:]
delta = windowed_measurements[1:] - windowed_measurements[:-1]
increases = np.sum(delta > 0)
print(increases)