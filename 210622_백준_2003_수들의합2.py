import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
i, j, ans, bound = 0, 0, 0, 0

while True:  # i이상 j미만의 bound를 확인할 것임
    if bound == m:  # 먼저 지금 값이 정답인지 확인
        ans += 1

    if bound >= m:
        bound -= a[i]
        i += 1
    elif j == n:  # 특정 i부터 j미만값까지 봤는데, j가 N이야. 즉 끝까지 간거지
        break  # 근데 값이 이미 M보다 작아, 그럼 할 수 있는 건 i를 늘리는 것 밖에. 근데 그건 무조건 작지
    else:
        bound += a[j]
        j += 1

print(ans)