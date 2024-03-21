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
# We should cover array `[a1,..,am]` by `n` ordered ranges `[li, ri]` with intersection in `<=1` symbols

def solve():
    n, m = map(int, input().strip().split())
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0] = [1 for _ in range(m)]
    # dp[n-1][m-1] - count of ways to cover directions `a1, ..., am` by `range 1, ..., range n`
    for i in range(1, n):
        for j in range(m):
            dp[i][j] += 2 * sum(dp[i - 1][:j])  # we can intersect previous or not
            dp[i][j] += dp[i - 1][j]  # we should intersect
    print(dp[-1][-1])


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