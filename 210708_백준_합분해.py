from pprint import pprint

n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
mod = int(1e9)
for i in range(n + 1):
    dp[1][i] = 1


for i in range(2, k + 1):
    for j in range(n + 1):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % mod

print(dp[k][n] % mod)
