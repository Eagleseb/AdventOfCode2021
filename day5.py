import numpy as np


def split_line(line: str):
    start, end = line.split(" -> ")
    return np.array(start.split(",") + end.split(","), dtype=int)


def generate_line_coordinates(line):
    x1, y1, x2, y2 = line
    while x1 != x2 or y1 != y2:
        yield x1, y1
        if x1 < x2:
            x1 += 1
        elif x1 > x2:
            x1 -= 1
        if y1 < y2:
            y1 += 1
        elif y1 > y2:
            y1 -= 1
    yield x1, y1


with open('resources/day5') as file:
    coordinates = np.array(list(map(split_line, file.readlines())))


def main():
    # Step 1
    horizontal = coordinates[coordinates[:, 1] == coordinates[:, 3]]
    vertical = coordinates[coordinates[:, 0] == coordinates[:, 2]]

    count = np.zeros([1000, 1000])

    for line in horizontal.tolist() + vertical.tolist():
        for x, y in generate_line_coordinates(line):
            count[x, y] += 1

    print(np.count_nonzero(count > 1))

    # Step 2
    diagonal = coordinates[(coordinates[:, 1] != coordinates[:, 3]) * (coordinates[:, 0] != coordinates[:, 2])]

    for line in diagonal:
        for x, y in generate_line_coordinates(line):
            count[x, y] += 1

    print(np.count_nonzero(count > 1))


if __name__ == '__main__':
    main()
