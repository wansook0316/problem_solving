import sys
from pprint import pprint

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# dp[i][j] = 4방향에서 발생하는 가능한 경로의 합(단, graph[i][j] > graph의 다음 경로 : 즉, 가능한 경로)


def DFS(y, x):
    dp[y][x] = 0  # 해당 함수의 호출 이유는, 해당 지점으로 부터 경로를 구하라는 것임 : 경로 개수는 0개일 수 있음
    if y == n - 1 and x == m - 1:  # 경로를 구하라고 했는데 도착지점이면 경로를 1로 업데이트 해줌
        dp[y][x] = 1
        return dp[y][x]

    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and graph[y][x] > graph[ny][nx]:
            if dp[ny][nx] == -1:  # 아직 방문하지 않았다면,
                dp[ny][nx] = DFS(ny, nx)
            dp[y][x] += dp[ny][nx]  # 이미 방문해서 탐색을 완료했다면, 그대로 더해줌
    return dp[y][x]


print(DFS(0, 0))
# pprint(dp)

# [
#     [3, 2, 2, 2, 1],
#     [1, -1, -1, 1, 1],
#     [1, -1, -1, 1, -1],
#     [1, 1, 1, 1, 1]
#     ]