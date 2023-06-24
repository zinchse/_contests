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


# Note: shortest path has an even length, it means that the distances to the cell from the horses are the same

def solve():
    from collections import deque
    pos1, pos2 = input().strip().split()
    distances1 = [[-1 for _ in range(8)] for _ in range(8)]
    distances2 = [[-1 for _ in range(8)] for _ in range(8)]
    queue1 = deque([(int(ord(pos1[0]) - ord('a')), int(pos1[1])-1, 0)])
    queue2 = deque([(int(ord(pos2[0]) - ord('a')), int(pos2[1])-1, 0)])

    def get_neighbors(i, j):
        res = []
        for di, dj in [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]:
            if 0 <= i+di < 8 and 0 <= j+dj < 8:
                res.append((i+di, j+dj))
        return res

    def dfs(queue, distances):
        while queue:
            i, j, d = queue.popleft()
            distances[i][j] = d
            for i_ngb, j_ngb in get_neighbors(i, j):
                if distances[i_ngb][j_ngb] == -1:
                    queue.append((i_ngb, j_ngb, d+1))

    dfs(queue1, distances1)
    dfs(queue2, distances2)
    print(min([distances1[i][j] for i in range(8) for j in range(8)
               if distances1[i][j] == distances2[i][j] and distances1[i][j] != -1], default=-1))


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
