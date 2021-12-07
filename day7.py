import numpy as np


def step1(crabs):
    distance = np.inf
    for i in range(crabs.max()):
        delta = np.abs(crabs - i)
        tmp = delta.sum()
        if tmp < distance:
            distance = tmp
    return distance


def step2(crabs):
    distance = np.inf
    for i in range(crabs.max()):
        delta = np.abs(crabs - i)
        tmp = (delta * (delta + 1) // 2).sum()
        if tmp < distance:
            distance = tmp
    return distance


def main():
    with open('resources/day7') as file:
        crabs = np.array(file.readline().split(","), dtype=int)

    print(step2(crabs))


if __name__ == '__main__':
    main()
