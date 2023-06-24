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
    N, M = map(int, input().strip().split())
    neighbors = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, input().strip().split())
        neighbors[v].append(u)

    colors = [0 for _ in range(N+1)]

    sys.setrecursionlimit(10 ** 9)
    def dfs(u, ans):
        ans.append(u)
        colors[u] = 1
        for v in neighbors[u]:
            if colors[v] == 0:
                dfs(v, ans)

    res = []
    dfs(1, res)
    print(' '.join(map(str, sorted(res))))


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
