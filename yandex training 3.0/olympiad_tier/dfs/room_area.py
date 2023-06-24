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
    N = int(input())
    labyrinth = [[] for _ in range(N)]
    for _ in range(N):
        labyrinth[_] = list(input().strip())

    def get_neighbors(x, y):
        res = []
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if 0 <= x+dx < N and 0 <= y+dy < N:
                res.append((x+dx, y+dy))
        return res

    colors = [[0 for _ in range(N)] for _ in range(N)]

    sys.setrecursionlimit(10 ** 9)
    def dfs(cur_v, area):
        cur_x, cur_y = cur_v
        colors[cur_y][cur_x] = 1
        area += 1
        for ngb_x, ngb_y in get_neighbors(cur_x, cur_y):
            if labyrinth[ngb_y][ngb_x] == '.' and colors[ngb_y][ngb_x] == 0:
                area = dfs((ngb_x, ngb_y), area)
        return area

    start_x, start_y = map(int, input().strip().split())
    print(str(dfs((start_x - 1, start_y - 1), 0)))


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