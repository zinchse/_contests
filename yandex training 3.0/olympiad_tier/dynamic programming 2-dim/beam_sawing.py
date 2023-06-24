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
    L, N = map(int, input().strip().split())
    # additional places to make task more convenient
    places = [0] + list(map(int, input().strip().split())) + [L]
    dp = [[float('inf') for _ in range(N + 2)] for _ in range(N + 2)]

    for l in range(N+1):
        dp[l][l + 1] = 0

    # fill dp[l, r] in ascending order `d = r - l`
    for d in range(N + 2):
        for l in range(N + 2):
            max_r = min(N + 1, l + d)
            for r in range(l, max_r + 1):
                dp[l][max_r] = min(dp[l][max_r], dp[l][r] + dp[r][max_r] + places[max_r] - places[l])

    print(dp[0][-1])


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
