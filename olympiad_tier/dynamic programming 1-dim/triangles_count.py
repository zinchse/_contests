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


# Idea
# Let's count separately the number of `upper` and `lower` triangles (`upper` are triangles with the base above the
# nose and `lower` are triangles with the base below)

def solve():
    N = int(input())

    upper_triangles = 0
    lower_triangles = 1

    for level in range(2, N + 1):
        points = level + 1

        # number of 2-combinations from `points`
        lower_triangles += points * (points - 1) // 2

        # nose may be in `pos = 1 ... points`, and may have `pos - 1` triangles
        # we can calculate this by symmetry and sum of arithmetic progression
        start_pos = 1
        end_pos = points // 2
        progression_len = points // 2
        progression_sum = (start_pos - 1 + end_pos - 1) * progression_len // 2
        upper_triangles += 2 * progression_sum
        if (level + 1) % 2 == 1:
            central_pos = points // 2 + 1
            upper_triangles += central_pos - 1

    print(upper_triangles+lower_triangles)


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
