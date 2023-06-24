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
# We depend only on the part of the previous part of the matrix separated from us by the side diagonal

def solve():
    N, M = map(int, input().strip().split())

    def check_id(i, j):
        return 0 <= i < N and 0 <= j < M

    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp[0][0] = 1

    def fill_dp(i, j):
        neighbors = [(-2, 1), (-2, -1), (-1, -2), (1, -2)]
        for neighbor in neighbors:
            if check_id(i + neighbor[0], j + neighbor[1]):
                dp[i][j] += dp[i + neighbor[0]][j + neighbor[1]]

    # diagonals from the left side
    for row in range(N):
        for col in range(min(row + 1, M)):
            fill_dp(row - col, col)

    # diagonals from the bottom side
    for col in range(1, M):
        for row in range(min(N, M - col)):
            fill_dp(N - 1 - row, col + row)

    print(dp[N-1][M-1])


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