def solution(prices):
    # prices = [4, 3, 1, 4, 5, 2, 7, 2, 3, 4]
    # prices = [1, 2, 3, 2, 3, 1]
    reverse_prices = prices[::-1]
    stack, ans = [], []
    for i in range(len(reverse_prices)):
        now = reverse_prices[i]
        if not stack:
            ans.append(0)
            stack.append(now)
            continue
        last = stack[-1]

        if now <= last:
            # 앞으로 가면서 찾아
            idx, count = len(stack) - 1, 0
            while idx >= 0:
                if stack[idx] < now:
                    break
                count += 1
                idx -= 1
            if idx < 0:
                ans.append(count)
            else:
                ans.append(count + 1)
            stack.append(now)
        else:
            ans.append(1)
            stack.append(now)
    return ans[::-1]