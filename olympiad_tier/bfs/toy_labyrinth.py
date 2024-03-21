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
    from collections import deque
    N, M = map(int, input().strip().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().strip().split())))

    def get_neighbors(start_i, start_j):
        res = []
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i_, j_ = start_i, start_j
            while 0 <= i_+di < N and 0 <= j_+dj < M and graph[i_+di][j_+dj] != 1:
                i_ += di
                j_ += dj
            res.append((i_, j_, di, dj))
        return res

    distances = [[-1 for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0, 1, 0, 0)])

    while queue:
        i, j, di, dj, d = queue.popleft()
        temp_i, temp_j = i, j
        while 0 <= temp_i < N and 0 <= temp_j < M and graph[temp_i][temp_j] != 1:
            if graph[temp_i][temp_j] == 2:
                print(d)
                return
            temp_i -= di
            temp_j -= dj

        if distances[i][j] == -1:
            distances[i][j] = d
            for ngb_info in get_neighbors(i, j):
                queue.append((*ngb_info, d+1))


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
