import sys
from pprint import pprint
from itertools import chain

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[1 for _ in range(n)] for _ in range(n)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
order = []
for i in range(n):
    for j in range(n):
        order.append([graph[i][j], [i, j]])
order.sort()

for o in order:
    trees, coord = o
    cy, cx = coord
    for (
        dy,
        dx,
    ) in d:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < n and 0 <= nx < n and trees > graph[ny][nx]:
            visited[cy][cx] = max(visited[cy][cx], visited[ny][nx] + 1)

print(max(list(chain(*visited))))