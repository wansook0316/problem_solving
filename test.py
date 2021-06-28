import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

i, j, _sum, ans = 0, 0, 0, 0

while True:
    if _sum == m:
        ans += 1

    if _sum >= m:
        _sum -= a[i]
        i += 1
    elif j == n:
        break
    else:
        _sum += a[j]
        j += 1

print(ans)