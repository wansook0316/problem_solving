from collections import deque
import sys

input = sys.stdin.readline
MAXNUM = 1e6
N, K = map(int, input().split())
visited = [False] * int(MAXNUM + 1)
minTime, minTimeNumOfVisited = 1e6, 0


def BFS():
    global minTime, minTimeNumOfVisited
    q = deque()
    q.append((N, 0))

    while q:
        pos, time = q.popleft()
        visited[pos] = True

        if time > minTime:
            continue  # 애초에 현재걸린시간이 최소시간보다 크면 탐색할 이유가 없음

        if pos == K:
            minTime = min(minTime, time)  # 처음 방문하면 여기서 걸리게 되어있음
            minTimeNumOfVisited += 1

        nexts = [(pos - 1, time + 1), (pos + 1, time + 1), (2 * pos, time + 1)]
        for npos, ntime in nexts:
            if 0 <= npos <= MAXNUM and visited[npos] == False:
                q.append((npos, ntime))


BFS()
print(minTime)
print(minTimeNumOfVisited)