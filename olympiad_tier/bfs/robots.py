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


# Comments: python's limits for this task are bad, we should use some local optimizations


def solve():
    from collections import deque

    N, K = map(int, input().strip().split())

    # optimization: store only unique neighbors
    neighbors = [set() for _ in range(N + 1)]
    for _ in range(K):
        u, v = map(int, input().strip().split())
        neighbors[u].add(v)
        neighbors[v].add(u)

    M = int(input())
    robots = tuple(map(int, input().strip().split()))
    # we will store the lengths of odd and even paths separately
    all_distances = [[] for _ in range(N+1)]

    def bfs(queue, distances):
        while queue:
            u, d = queue.popleft()
            if distances[u][0] == 4 * N and d % 2 == 1:
                distances[u] = (d, distances[u][1])
                for v in neighbors[u]:
                    if distances[v][1] == 4 * N:
                        queue.append((v, d + 1))
            elif distances[u][1] == 4 * N and d % 2 == 0:
                distances[u] = (distances[u][0], d)
                for v in neighbors[u]:
                    if distances[v][0] == 4 * N:
                        queue.append((v, d + 1))

    for i in range(M):
        # optimization: store one array of tuples
        distances = [(4 * N, 4 * N) for _ in range(N+1)]
        bfs(deque([(robots[i], 0)]), distances)
        for u in range(1, N+1):
            all_distances[u].append(distances[u])

    vertex_res = 4 * N
    for u in range(1, N + 1):
        vertex_res = min(vertex_res, max([all_distances[u][robot][0] for robot in range(M)]))
        vertex_res = min(vertex_res, max([all_distances[u][robot][1] for robot in range(M)]))

    edge_res = 4 * N
    for u in range(1, N+1):
        for v in neighbors[u]:
            if u < v:
                max_distance_u, max_distance_v = 0, 0
                for r in range(M):
                    distance_u = min(all_distances[u][r][0], all_distances[u][r][1])
                    distance_v = min(all_distances[v][r][0], all_distances[v][r][1])
                    if distance_u < distance_v:
                        max_distance_u = max(max_distance_u, distance_u)
                    else:
                        max_distance_v = max(max_distance_v, distance_v)
                    # optimization: break search process if some robot takes a long time to go to that point
                    if 2 * max(max_distance_u, max_distance_v) + 1 >= edge_res:
                        break
                edge_res = min(edge_res, 2 * max(max_distance_u, max_distance_v) + 1)

    if edge_res == 4 * N and vertex_res == 4 * N:
        print(-1)
    else:
        print(min(vertex_res, edge_res / 2.0))


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
