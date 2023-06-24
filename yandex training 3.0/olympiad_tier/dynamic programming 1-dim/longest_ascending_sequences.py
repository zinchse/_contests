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
    array = list(map(int, input().strip().split()))
    dp = [1] * N
    id_max = 0
    m = 1
    for i, val in enumerate(array):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        if m < dp[i]:
            m = dp[i]
            id_max = i

    res = [array[id_max]]
    cur_dp = m
    for i in range(id_max, -1, -1):
        if res[-1] > array[i] and dp[i] == cur_dp - 1:
            cur_dp -= 1
            res.append(array[i])

    print('\n'.join(map(str, res[::-1])))


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