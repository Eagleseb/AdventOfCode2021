import numpy as np


def to_binary(x: np.array) -> int:
    return int("".join(x.astype(str)), base=2)


with open('resources/day3') as file:
    measure = np.array([list(map(int, line[:-1])) for line in file.readlines()])

avgbit = measure.mean(0).round().astype(int)
# step 1
gamma = to_binary(avgbit)
epsilon = to_binary(1 - avgbit)
print(gamma * epsilon)

# step 2
measure_ox = measure
measure_sc = measure

for i in range(measure.shape[1]):
    most_common_bit = measure_ox[:, i].mean() >= .5
    measure_ox = measure_ox[measure_ox[:, i] == most_common_bit]
    least_common_bit = 1 - measure_sc[:, i].mean() > .5
    tmp = measure_sc[measure_sc[:, i] == least_common_bit]
    if len(tmp) > 0:
        measure_sc = tmp

oxygen = to_binary(measure_ox[0])
scrubber = to_binary(measure_sc[0])
print(oxygen * scrubber)
