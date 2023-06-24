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
# Definitely, we have to cover all vertices, hence the vertex with the minimal `height'.
# Who can cover them? Only neighboring vertices with the same `height'. We can choose any of them.
# After that we will cover other vertices, we need to take this into account.
# The algorithm looks like iteratively covering the remaining vertices in order of their `heights`, until
# we cover the whole military field.

def solve():
    N, M = map(int, input().strip().split())
    G = [[] for _ in range(N)]
    heights = [[] for _ in range(10001)]
    for y in range(N):
        G[y] = list(map(int, input().strip().split()))
        for x, height in enumerate(G[y]):
            heights[height].append((x, y))

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x+dx < M and 0 <= y+dy < N:
                neighbors.append((x+dx, y+dy))
        return neighbors

    visited = [[False for _ in range(M)] for _ in range(N)]

    sys.setrecursionlimit(2 * 100 * 100 + 3)
    def dfs(cur_x, cur_y):
        visited[cur_y][cur_x] = True
        for x_ngb, y_ngb in get_neighbors(cur_x, cur_y):
            if G[y_ngb][x_ngb] >= G[cur_y][cur_x] and not visited[y_ngb][x_ngb]:
                dfs(x_ngb, y_ngb)

    res = 0
    for height_list in heights:
        for x, y in height_list:
            if not visited[y][x]:
                res += 1
                dfs(x, y)
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
