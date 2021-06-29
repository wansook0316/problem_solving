# dp[n] = n까지의 원소를 포함했을 때, 가장 긴 증가하는 부분 수열의 길이
# dp[n] = dp[1~n-1] + 1 (만약 가능할 경우)

import sys

input = sys.stdin.readline

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(1, i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
