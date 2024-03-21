import os.path
import sys

INTO_FILE = False
output = []


def fast_input(file_name):
    global INTO_FILE
    if os.path.isfile(file_name):
        INTO_FILE = True
        with open(file_name, 'r') as file:
            input_lines = file.readlines()
    else:
        INTO_FILE = False
        input_lines = sys.stdin.readlines()

    for line in input_lines:
        yield line


fast_input_reader = fast_input('input.txt')


def input():
    return fast_input_reader.__next__()


def print(line):
   output.append(str(line))


def solve():
    from collections import deque
    value1 = int(input().strip())
    value2 = int(input().strip())

    distances = [-1 for _ in range(10000)]

    def get_neighbors(value):
        neighbors = [int(str(value)[1:] + str(value)[0]), int(str(value)[-1] + str(value)[:-1])]
        if value % 10 > 1:
            neighbors.append(value - 1)
        if value // 1000 < 9:
            neighbors.append(value + 1000)
        return neighbors

    def get_inverted_neighbors(value):
        neighbors = [int(str(value)[1:] + str(value)[0]), int(str(value)[-1] + str(value)[:-1])]
        if value % 10 < 9:
            neighbors.append(value + 1)
        if value // 1000 > 1:
            neighbors.append(value - 1000)
        return neighbors

    queue = deque([(value1, 0)])

    while queue:
        value, d = queue.popleft()
        if distances[value] == -1:
            distances[value] = d
            for ngb in get_neighbors(value):
                queue.append((ngb, d+1))

    distance = distances[value2]
    cur_value = value2
    res = []
    while distance != -1:
        res.append(cur_value)
        distance -= 1
        for ngb in get_inverted_neighbors(cur_value):
            if distances[ngb] == distance:
                cur_value = ngb
    print(' '.join(map(str, res[::-1])))


def main():
    solve()
    answer = '\n'.join(output) + '\n'

    if INTO_FILE:
        with open('output.txt', 'w') as output_file:
            output_file.write(answer)
    else:
        sys.stdout.write(answer)


if __name__ == '__main__':
    main()