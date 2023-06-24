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
    N = int(input().strip())
    times = [tuple(map(int, input().strip().split())) for _ in range(N)]
    MAX_TIME = sum([time[0] for time in times])
    dp = [[0 for _ in range(MAX_TIME + 1)] for _ in range(N + 1)]

    for item in range(1, N + 1):
        a, b = times[item - 1]
        for time in range(MAX_TIME + 1):
            dp[item][time] = dp[item - 1][time] + b
            if time - a >= 0:
                dp[item][time] = min(dp[item - 1][time - a], dp[item][time])

    answers = [max(dp[N][time], time) for time in range(MAX_TIME + 1)]
    res = min(answers)

    index = answers.index(res)
    path = []
    for item in range(N, 0, -1):
        a, b = times[item - 1]
        if dp[item][index] == dp[item - 1][index] + b:
            path.append(2)

        else:
            path.append(1)
            index -= a

    print(' '.join(map(str, path[::-1])))


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
