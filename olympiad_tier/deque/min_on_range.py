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
    N, K = map(int, input().strip().split())
    array = list(map(int, input().strip().split()))

    d = deque()
    res = []

    for i in range(N):
        if len(d) and d[0][1] == i - K:
            d.popleft()

        cur_item = array[i]
        while len(d) and d[-1][0] > cur_item:
            d.pop()
        d.append((cur_item, i))

        if i >= K - 1:
            res.append(d[0][0])

    print('\n'.join(map(str, res)))


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
