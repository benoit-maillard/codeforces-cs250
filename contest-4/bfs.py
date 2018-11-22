from math import *
from sys import stdin
from collections import deque

# all indexes start at 0 in this function (including i)
def bfs(n, m, i, edges):
    adj = [] # TODO : why [[]]*n does not work
    shortest_path = []

    for j in range(0, n):
        adj.append([])
        shortest_path.append(inf)

    shortest_path[i] = 0

    for k in range(0, m):
        adj[edges[k][0]].append(edges[k][1])
        adj[edges[k][1]].append(edges[k][0])

    queue = deque([i])

    while len(queue) != 0:
        v = queue.popleft()
        for u in adj[v]:
            if (shortest_path[u]) == inf:
                shortest_path[u] = shortest_path[v] + 1
                queue.append(u)

    return shortest_path

lines = stdin.read().split("\n")

# make sure there is no empty line at the end
if lines[-1] == '':
    lines.pop()

values_n = [int(v) for v in lines[0].split(" ")]
n = values_n[0]
m = values_n[1]
i = values_n[2] - 1



edges = [[int(v) - 1 for v in l.split(" ")] for l in lines[1:]]

print(*bfs(n, m, i, edges))
