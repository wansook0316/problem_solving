import sys
from pprint import pprint

input = sys.stdin.readline

n = int(input())
m = int(input())
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dp[i][k] and dp[k][j]:
                dp[i][j] = 1

for i in range(1, n + 1):
    ans = 0
    for j in range(1, n + 1):
        if i == j:
            continue
        if dp[i][j] == 0 and dp[j][i] == 0:
            ans += 1
    print(ans)
