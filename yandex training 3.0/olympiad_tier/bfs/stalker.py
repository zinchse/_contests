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


fast_input_reader = fast_input('18_40a.txt')


def input():
    return fast_input_reader.__next__()

def print(line):
    output.append(str(line))


# Comments: python's limits for this task are bad, we should use some special optimizations
# Idea:
# 1) represent fixed map as a set of connected components (to reduce the size of vertex from `N * # maps`
#    to `N + # components`)
# 2) note that it is the state graph `<component, current map>`
# 3) introduce a dummy nodes `<place, empty_map>`, when `empty_map` is a map without any connections;
#    then all transitions can be performed only through the vertex `<place, empty_map>`:
#    `<place, map1>`->`<place map2>`==`<place, empty_map>`->`<place, map1>->`<place, empty_map>`->`<place, map2>`
#    it allows to us reduce the number of edges from `N * N` to `N * # components`.
# 4) then our task is 0-1 BFS (0 is a cost of transition `<place, mapi> -> <place, empty_map>`)


def solve():
    from collections import deque, defaultdict

    N, K = map(int, input().strip().split())
    START, END = 1, N
    EMPTY_MAP = 0
    sys.setrecursionlimit(10 ** 9)

    def dfs(cur_v, prev_v, cur_component, visited):
        visited[cur_v] = True
        cur_component.add(cur_v)
        for u in neighbors[cur_v]:
            if u != prev_v and not visited[u]:
                dfs(u, cur_v, cur_component, visited)

    # connected component for `empty_map` is just the vertex itself
    components = [(set([i]), EMPTY_MAP) for i in range(N+1)]
    cur_comp = N + 1

    graph = [[] for _ in range(N+1)]
    end_comps, start_comps = [], []

    # iterating over the maps
    for k in range(1, K+1):
        neighbors = [[] for _ in range(N+1)]
        r = int(input())
        # reading the roads
        for i in range(r):
            u, v = map(int, input().strip().split())
            neighbors[u].append(v)
            neighbors[v].append(u)
        visited = [False for _ in range(N+1)]
        # looking for connected components in current map
        for v in range(1, N + 1):
            if not visited[v]:
                component = set()
                dfs(v, 0, component, visited)
                # connected component is usefully only if its size > 1
                if len(component) > 1:
                    if START in component:
                        start_comps.append(cur_comp)
                    if END in component:
                        end_comps.append(cur_comp)
                    components.append((component, k))
                    graph.append([])
                    # connecting previous components with current one
                    for u in component:
                        graph[u].append(cur_comp)
                        graph[cur_comp].append(u)
                    cur_comp += 1

    distances = defaultdict(lambda: -1)
    queue = deque([(1, 0)])
    while queue:
        c, d = queue.popleft()
        if distances[c] == -1:
            distances[c] = d
            for new_c in graph[c]:
                if distances[new_c] == -1:
                    # we can delete map free
                    if components[new_c][1] == EMPTY_MAP:
                        queue.appendleft((new_c, d))
                    elif components[c][1] == EMPTY_MAP:
                        queue.append((new_c, d + 1))

    print(min([distances[j] for j in end_comps if distances[j] != -1], default=-1))


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