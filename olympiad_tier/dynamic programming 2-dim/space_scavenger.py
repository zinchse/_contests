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
    chars = ['N', 'S', 'W', 'E', 'U', 'D']
    rules = {}
    dp = {}
    for char in chars:
        rules[char] = input().strip()
    command, param = input().strip().split()
    for char in chars:
        dp[char] = [0] * (int(param) + 1)
    for value in range(1, int(param) + 1):
        for char in chars:
            rule = rules[char]
            dp[char][value] += 1
            for c in rule:
                dp[char][value] += dp[c][value - 1]
    print(dp[command][-1])


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
