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
    import math

    x_l, x_r = map(int, input().strip().split())
    R = int(input())
    N = int(input())
    palms = []
    for _ in range(N):
        x, y = map(int, input().strip().split())
        palms.append((x, y))

    distances = [[0] * (N + 2) for _ in range(N + 2)]
    left, right = N, N + 1
    distances[left][right] = distances[right][left] = x_r - x_l

    for i in range(N):
        xi, yi = palms[i]
        distances[i][left] = distances[left][i] = max(0.0, xi - R - x_l)
        distances[i][right] = distances[right][i] = max(0.0, x_r - xi - R)

        for j in range(N):
            xj, yj = palms[j]
            dx = xi - xj
            dy = yi - yj
            distances[i][j] = max(0.0, math.sqrt(dx * dx + dy * dy) - 2 * R)

    def is_connected(u_from, u_to, max_d):
        used = [False] * len(distances)

        def dfs(u):
            used[u] = True
            for v, d in enumerate(distances[u]):
                if not used[v] and d < max_d:
                    dfs(v)

        dfs(u_from)
        return not used[u_to]

    l, r = 0, distances[left][right]
    for it in range(50):
        d_mid = (l + r) / 2
        if is_connected(left, right, d_mid):
            l = d_mid
        else:
            r = d_mid

    print('{:.3f}'.format(l))


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
