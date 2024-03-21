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


# Idea:
# binsearch + bipartite check
def solve():
    import math
    N = int(input())
    towers = []
    for _ in range(N):
        towers.append(list(map(int, input().strip().split())))

    def get_distance(i, j):
        return (towers[i][0] - towers[j][0]) ** 2 + (towers[i][1] - towers[j][1]) ** 2

    sys.setrecursionlimit(10 ** 9)
    def dfs(v, color, K, visited, colors):
        visited[v] = True
        colors[v] = color
        for u in range(N):
            assert not (u != v and visited[u] and get_distance(v, u) < K and colors[u] == color)
            if not visited[u] and get_distance(v, u) < K:
                dfs(u, 3-color, K, visited, colors)

    def check_bipartite(K):
        visited = [False for _ in range(N)]
        colors = [1 for _ in range(N)]
        for v in range(N):
            if not visited[v]:
                dfs(v, 1, K, visited, colors)
        return colors

    max_x = max_y = 10 ** 4
    l, r = 0, (2 * max_x) ** 2 + (2 * max_y) ** 2 + 1
    while l < r:
        m = (l + r) // 2
        try:
            check_bipartite(m)
            l = m + 1
        except AssertionError:
            r = m

    print(f"{math.sqrt(l-1) / 2}")
    print(' '.join(map(str, check_bipartite(l-1))))


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
