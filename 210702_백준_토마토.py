import sys
from pprint import pprint
from collections import deque

input = sys.stdin.readline

INF = int(1e6)
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]


q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            # visited[i][j] = 0
            q.append([i, j])


while q:
    cy, cx = q.popleft()

    for dy, dx in d:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:

            graph[ny][nx] = graph[cy][cx] + 1
            q.append([ny, nx])

# pprint(visited)


answer = -10
flag = True
for i in range(n):
    for j in range(m):
        if flag:
            answer = max(answer, graph[i][j])
            if graph[i][j] == 0:
                answer = 0
                flag = False
print(answer - 1)
