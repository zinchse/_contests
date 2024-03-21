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
    N = int(input())
    for _ in range(N):
        try:
            stack = deque()
            N, *vals = map(float, input().strip().split())
            cur_max = float('-inf')
            for val in vals:
                while len(stack) and stack[-1] < val:
                    stack_val = stack.pop()
                    cur_max = max(cur_max, stack_val)
                assert cur_max <= val
                stack.append(val)
            print('1')
        except AssertionError:
            print('0')


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
