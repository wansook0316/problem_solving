# 안전영역 최대 개수
# visited -> 할때마다 초기화
# BFS 함수


import sys
from collections import deque
from itertools import chain
from pprint import pprint


def BFS(y, x):
    global n, visited
    q = deque()
    q.append([y, x])
    visited[y][x] = 1
    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while q:
        cy, cx = q.pop()

        for dy, dx in d:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                q.append([ny, nx])


input = sys.stdin.readline

n = int(input())
pool = []
for _ in range(n):
    pool.append(list(map(int, input().split())))
low, high = 0, max(chain(*pool))

answer = 0
for height in range(low, high + 1):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    safe_area = 0
    for i in range(n):
        for j in range(n):
            if pool[i][j] <= height:
                visited[i][j] = -1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                BFS(i, j)
                safe_area += 1
    answer = max(answer, safe_area)

print(answer)