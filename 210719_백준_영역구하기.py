import sys
from pprint import pprint
from collections import deque

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline


def DFS(y, x):
    board[y][x] = -1  # 방문한 곳 체크
    ret = 1  # 현재 방문한 곳의 count
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and board[ny][nx] == 0:
            ret += DFS(ny, nx)  # 현재 지역에서 방문할 수 있는 곳의 count를 모두 더한 것이 현재 넓이
    return ret


ans = []
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
m, n, k = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):

    x1, y1, x2, y2 = map(int, input().split())
    y1, y2 = m - y2, m - y1
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            count = DFS(i, j)
            ans.append(count)
ans.sort()
print(len(ans))
for a in ans:
    print(a, end=" ")