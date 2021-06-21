from collections import deque
import sys

# sys.setrecursionlimit(int(1e6))
# input = sys.stdin.readline

N, K = map(int, input().split())
visited = [-1] * 100001
path = []


def BFS():
    q = deque()
    q.append((N, 0))
    visited[N] = N

    while q:
        pos, time = q.popleft()
        if pos == K:
            a = pos
            while a != N:
                path.append(a)
                a = visited[a]
            path.append(a)
            return time

        if pos + 1 < 100001 and visited[pos + 1] == -1:
            q.append((pos + 1, time + 1))
            visited[pos + 1] = pos

        if pos - 1 >= 0 and visited[pos - 1] == -1:
            q.append((pos - 1, time + 1))
            visited[pos - 1] = pos

        if pos * 2 < 100001 and visited[pos * 2] == -1:
            q.append((pos * 2, time + 1))
            visited[pos * 2] = pos


print(BFS())
print(path[::-1])


from collections import deque
import sys

n, k = map(int, input().split())

visited = [-1] * 100001  # 방문여부까지 확인하기 위해 -1로 초기화
path = []  # 지금까지 방문 경로 저장


def bfs(start, target):
    queue = deque()
    queue.append((n, 0))
    visited[start] = start
    while queue:
        cur, cur_time = queue.popleft()
        if cur == target:  # 동생을 찾음
            idx = cur
            while idx != start:
                path.append(idx)
                idx = visited[idx]  # 이 부분이 중요!
            path.append(start)  # 첫 시작점까지 넣는다
            return cur_time
        if cur + 1 < 100001 and visited[cur + 1] == -1:
            queue.append((cur + 1, cur_time + 1))
            visited[cur + 1] = cur

        if cur - 1 >= 0 and visited[cur - 1] == -1:
            queue.append((cur - 1, cur_time + 1))
            visited[cur - 1] = cur

        if cur * 2 < 100001 and visited[cur * 2] == -1:
            queue.append((cur * 2, cur_time + 1))
            visited[cur * 2] = cur


print(bfs(n, k))
print(*path[::-1])  # 뒤에서 부터 출력


# 위의 코드가 왜안되는지 돚2ㅓ히 알 수가 없다.