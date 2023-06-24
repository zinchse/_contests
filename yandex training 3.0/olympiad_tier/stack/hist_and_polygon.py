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


# Idea:
# Meeting a new element, we remove anything smaller than it from the stack  -- we don't need the `height` of the deleted
# elements anymore, since they will be bounded either by the current element or by even smaller ones. However, the
# `pos` of the elements to be deleted need to be taken into account, as these are in `width` of future rectangles.
# At the same time, when deleting, we see if there's been a record in terms of area. There are elements left at the
# very end that no one limits to the right, to catch them we need to add `TRIGGER`.
#
# Time Complexity - O(n)
# Space Complexity - O(n)

def solve():
    from collections import deque

    N, *array = list(map(int, input().strip().split()))

    stack = deque()
    res = 0
    TRIGGER = [0]
    for pos, height in enumerate(array + TRIGGER, start=1):
        new_pos = pos
        while len(stack) and stack[-1][0] >= height:
            prev_height, prev_pos = stack.pop()
            prev_width = pos - prev_pos
            res = max(res, prev_height * prev_width)
            new_pos = prev_pos
        stack.append((height, new_pos))
    print(res)


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

