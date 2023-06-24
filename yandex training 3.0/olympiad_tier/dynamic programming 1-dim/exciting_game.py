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
    N, a, b = map(int, input().strip().split())
    if a < b:
        a, b = b, a
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    dp[1] = 0
    for n in range(2, N + 1):
        for i in range(1, n // 2 + 1):
            assert dp[n-i] >= dp[i]
            min_dp, max_dp = min(dp[n - i], dp[i]), max(dp[n - i], dp[i])
            worst_cost = max(min_dp + a, max_dp + b)
            dp[n] = min(dp[n], worst_cost)
    print(dp[-1])


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