# dp[n] = n까지의 원소를 포함했을 때, 가장 긴 증가하는 부분 수열의 길이
# dp[n] = dp[1~n-1] + 1 (만약 가능할 경우)

import sys

input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [[1, a[i]] for i in range(n + 1)]
max_length = 0
for i in range(2, n + 1):
    for j in range(1, i):
        if a[i] > a[j]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = max(dp[i][1], dp[j][1] + a[i])
            # dp[i][0] = max(dp[i], dp[j] + 1)

ans, index = 0, 0

for i in range(1, len(dp)):
    if ans < dp[i][1]:
        ans = dp[i][1]
print(ans)