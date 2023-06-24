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
    import heapq

    K, N = map(int, input().strip().split())

    free_stances = list(range(1, K + 1))
    heapq.heapify(free_stances)

    busy_stances = []

    res = []
    for train in range(1, N + 1):
        arrival_time, departure_time = map(int, input().strip().split())

        while busy_stances and busy_stances[0][0] < arrival_time:
            time, stance = heapq.heappop(busy_stances)
            heapq.heappush(free_stances, stance)

        if not free_stances:
            print(f"0 {train}")
            break

        free_stance = heapq.heappop(free_stances)
        res.append(str(free_stance))
        heapq.heappush(busy_stances, (departure_time, free_stance))

    else:
        print('\n'.join(res))


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
