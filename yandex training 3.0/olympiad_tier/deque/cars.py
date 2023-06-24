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
    from collections import defaultdict, deque
    import heapq

    N, K, P = map(int, input().strip().split())

    cars_positions = defaultdict(deque)
    cars_queue = []
    for i in range(P):
        car = int(input())
        cars_positions[car].append(i)
        cars_queue.append(car)

    floor = set()
    heap_pos = []
    res = 0

    for i, car in enumerate(cars_queue):
        cars_positions[car].popleft()
        next_pos = cars_positions[car][0] if cars_positions[car] else P

        if car in floor:
            heapq.heappush(heap_pos, (-next_pos, car))
            continue
        elif len(floor) < K:
            heapq.heappush(heap_pos, (-next_pos, car))

        else:
            latest_pos, latest_car = heapq.heappop(heap_pos)
            floor.remove(latest_car)
            heapq.heappush(heap_pos, (-next_pos, car))
        res += 1
        floor.add(car)

    print(str(res))


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
