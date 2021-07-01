def solution(n, times):
    def isOk(value):
        numOfPerson = 0
        i = 0
        while numOfPerson <= n and i < len(times):
            numOfPerson += value // times[i]
            i += 1

        if numOfPerson >= n:
            return True
        else:
            return False

    times.sort()
    left, right = 1, times[-1] * n
    while left < right:

        mid = (left + right) // 2
        if isOk(mid):
            right = mid
        else:  # 제안한 값이 넘치는 경우 10 > 6
            left = mid + 1

    return right