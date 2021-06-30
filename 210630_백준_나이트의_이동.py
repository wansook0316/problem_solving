import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ans = 0
    n = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    action = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = 0

    while q:
        cy, cx = q.popleft()
        if cy == end[0] and cx == end[1]:
            ans = visited[cy][cx]
            break

        for dy, dx in action:
            ny, nx = cy + dy, cx + dx

            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:
                visited[ny][nx] = visited[cy][cx] + 1
                q.append([ny, nx])

    print(ans)