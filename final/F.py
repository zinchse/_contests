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
    # read data
    H, W = map(int, input().strip().split())
    field = []
    for _ in range(H):
        field.append(input().strip())
    start_x, start_y = map(int, input().strip().split())
    end_x, end_y = map(int, input().strip().split())

    # build infrastructure
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    MAX_DISTANCE = H * W + 1
    MAX_W, MAX_N_DIR = 1000 * 10, 10
    distances = [[[MAX_DISTANCE for _ in directions] for _ in range(W)] for _ in range(H)]
    queue = deque([])
    for dir_index, _ in enumerate(directions):
        distances[H - start_y][start_x - 1][dir_index] = 1
        code = ((H - start_y) * MAX_W + (start_x - 1)) * MAX_N_DIR + dir_index
        queue.append(code)

    # loop
    res = -1
    while queue:
        code = queue.popleft()
        i, j, dir_index = code // (MAX_W * MAX_N_DIR), (code // MAX_N_DIR) % MAX_W, code % MAX_N_DIR
        d = distances[i][j][dir_index]

        if (i, j) == (H - end_y, end_x - 1):
            res = d
            break

        # 0-edge
        di, dj = directions[dir_index]
        if 0 <= i + di < H and 0 <= j + dj < W and field[i + di][j + dj] == '.':
            dir_index = directions.index((di, dj))
            if d < distances[i + di][j + dj][dir_index]:
                distances[i + di][j + dj][dir_index] = d
                queue.appendleft(((i + di) * MAX_W + (j + dj)) * MAX_N_DIR + dir_index)

        # 1-edge
        for di_, dj_ in directions:
            if 0 <= i + di_ < H and 0 <= j + dj_ < W and field[i + di_][j + dj_] == '.':
                dir_index = directions.index((di_, dj_))
                if distances[i + di_][j + dj_][dir_index] == MAX_DISTANCE:
                    distances[i + di_][j + dj_][dir_index] = d + 1
                    queue.append(((i + di_) * MAX_W + (j + dj_)) * MAX_N_DIR + dir_index)

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

