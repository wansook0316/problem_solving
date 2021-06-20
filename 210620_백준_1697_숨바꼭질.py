from collections import deque
import sys


input = sys.stdin.readline

MAXNUM = 1e6
N, K = map(int, input().split())
visited = [False] * int(MAXNUM + 1)


def BFS():
    q = deque()
    q.append((N, 0))  # position, cost

    while q:
        pos, cost = q.popleft()
        visited[pos] = True

        if pos == K:
            return cost

        nexts = [(pos - 1, cost + 1), (pos + 1, cost + 1), (2 * pos, cost + 1)]

        for npos, ncost in nexts:
            if 0 <= npos <= MAXNUM and visited[npos] == False:
                q.append((npos, ncost))


ans = BFS()
print(ans)