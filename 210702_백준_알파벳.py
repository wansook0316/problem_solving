# BFS로 최단거리를 구하는 것이 아니기 때문에 굳이 queue일 필요가 없다.
# 순서에 상관없이 완전 탐색을 하는 것이 목적!!

import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(r)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
max_value = 0

q = set()
q.add((0, 0, graph[0][0]))

while q:
    cy, cx, memory = q.pop()

    max_value = max(max_value, len(memory))

    for dy, dx in d:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] not in memory:
            q.add((ny, nx, memory + graph[ny][nx]))

print(max_value)