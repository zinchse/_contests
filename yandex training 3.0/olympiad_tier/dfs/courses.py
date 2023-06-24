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


# Idea
# We want to take maximal lexicographical topological sort `c1 ... cn`. But all algorithms of finding topological sort
# construct it from the end. Let's reverse graph, and build topological sort in order of value of current leaf nodes.
# We have to manage count of degrees and heap.

def solve():
    import heapq
    N = int(input())
    neighbors, deg_in = [[] for _ in range(N+1)], [0 for _ in range(N+1)]

    for i in range(1, N+1):
        k, *raw_list_v = map(int, input().strip().split())
        list_v = list(raw_list_v)
        for v in list_v:
            neighbors[i].append(v)
            deg_in[v] += 1

    heap = [-i for i in range(1, N+1) if not deg_in[i]]
    heapq.heapify(heap)

    res = []
    while heap:
        v = -heapq.heappop(heap)
        res.append(v)
        for u in neighbors[v]:
            deg_in[u] -= 1
            if deg_in[u] == 0:
                heapq.heappush(heap, -u)

    print(' '.join(map(str, res[::-1])))


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
