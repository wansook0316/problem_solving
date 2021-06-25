def solution(prices):
    ans, stack = [0] * len(prices), []

    for now, price in enumerate(prices):
        if stack:
            while (
                stack and price < prices[stack[-1]]
            ):  # 스택안에 원소가 있고, 현재가격이 이전 가격보다 떨어졌다면
                past = stack.pop()
                ans[past] = now - past
        stack.append(now)
    for (
        i
    ) in (
        stack
    ):  # 이제 스택은 비내림차순으로 정렬되어 있다. 그리고 그 안의 원소는 시간임. 지금까지 살아있는 원소는 끝까지 돌았는데도 남아있는 것들임
        ans[i] = len(prices) - (i + 1)  # 총 시간에서 해당 가격의 시간을 빼준다.
    return ans
