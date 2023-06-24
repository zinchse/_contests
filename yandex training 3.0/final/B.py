import os.path
import sys
# hello
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
    from heapq import heappush, heappop
    N, W = map(int, input().strip().split())

    tasks = []
    for i in range(1, N + 1):
        start, long = map(int, input().strip().split())
        tasks.append((start, long))

    tasks = sorted(enumerate(tasks), key=lambda x: (x[1][0]))
    workers = []

    for i, (start, duration) in tasks:
        if not workers or workers[0][0] > start:
            heappush(workers, (start + duration, [i + 1]))
        elif workers[0][0] <= start:
            worker = heappop(workers)
            task_list = worker[1][:]
            task_list.append(i + 1)
            worker = (start + duration, task_list)
            heappush(workers, worker)

    print(len(workers))
    print(' '.join(map(str, [i for x in workers for i in x[1]])))

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
