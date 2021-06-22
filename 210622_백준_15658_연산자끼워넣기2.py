import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
state = {"+": plus, "-": minus, "*": multi, "/": div}
maxNum, minNum = -1e11, 1e11


def go(idx, value):
    global maxNum, minNum
    if idx == n:
        maxNum = max(maxNum, value)
        minNum = min(minNum, value)
        return

    for op in "+-*/":
        if state[op]:
            state[op] -= 1
            go(idx + 1, int(eval(f"{value}{op}{a[idx]}")))
            state[op] += 1


go(1, a[0])
print(maxNum)
print(minNum)
