def solution(N, number):
    # 사용한 N의 개수를 기반으로 만들 수 있는 수를 넣어둠
    # 일단 사용할 수 있는 N의 개수는 8이하기 때문에 8개의 공간이 생길 예정

    # dp[i] = i번 N을 사용하여 만들 수 있는 수

    dp = [set([int(str(N) * x)]) if x != 0 else 0 for x in range(9)]

    for i in range(2, 9):
        for j in range(1, i):  # j, i-j

            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    if a - b >= 0:
                        dp[i].add(a - b)
                    else:
                        dp[i].add(b - a)
                    dp[i].add(a * b)

                    if b != 0 and a % b == 0:
                        dp[i].add(int(a / b))
                    if a != 0 and b % a == 0:
                        dp[i].add(int(b / a))
    answer = -1
    for i in range(1, len(dp)):
        if number in dp[i]:
            answer = i
            break
    return answer