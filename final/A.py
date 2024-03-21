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
    from collections import deque, defaultdict
    N = int(input())
    d = defaultdict(int)
    heap = deque()
    for _ in range(N):

        command = input().strip().split()

        if command[0] == 'add':
            count = int(command[1])
            tip = command[2]
            heap.append((count, tip))
            d[tip] += count

        elif command[0] == 'get':
            print(d[command[1]])

        elif command[0] == 'delete':
            count = int(command[1])
            while count > 0:
                cur_count, tip = heap.pop()
                if cur_count > count:
                    d[tip] -= count
                    cur_count -= count
                    heap.append((cur_count, tip))
                    break
                else:
                    d[tip] -= cur_count
                    count -= cur_count




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
