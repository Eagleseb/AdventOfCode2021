import numpy as np

with open('resources/day6') as file:
    fish = np.array(file.readline().split(","), dtype=int)

# step 1
# for i in range(80):
#     fish -= 1
#     giving_birth = fish == -1
#     birth_count = np.count_nonzero(giving_birth)
#     fish[giving_birth] = 6
#     fish = np.append(fish, birth_count * [8])

# step 2
counts = np.zeros(9, dtype=np.int64)
for i in range(9):
    counts[i] = np.count_nonzero(fish == i)
for i in range(256):
    tmp = np.empty_like(counts)
    tmp[0:-1] = counts[1:]
    tmp[8] = counts[0]
    tmp[6] += counts[0]
    counts = tmp

print(counts.sum())
