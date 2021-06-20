from collections import deque
import sys


input = sys.stdin.readline

MAXNUM = 1e6
N, K = map(int, input().split())
visited = [False] * int(MAXNUM + 1)
ans = 1e6


def BFS():
    global ans
    q = deque()
    q.append((N, 0))  # position, cost

    while q:
        pos, cost = q.popleft()
        visited[pos] = True

        if cost > ans:
            continue

        if pos == K:
            ans = min(ans, cost)

        nexts = [(pos - 1, cost + 1), (pos + 1, cost + 1), (2 * pos, cost)]
        for npos, ncost in nexts:
            if 0 <= npos <= MAXNUM and visited[npos] == False:
                q.append((npos, ncost))

BFS()
print(ans)
