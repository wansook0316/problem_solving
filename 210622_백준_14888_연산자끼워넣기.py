import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())
state = ["+"] * plus + ["-"] * minus + ["*"] * multi + ["/"] * div

opList = set(permutations(state, len(state)))
maxNum, minNum = -1e11, 1e11
for operations in opList:
    ans = a[0]
    for op, num in zip(operations, a[1:]):
        ans = int(eval(f"{ans}{op}{num}"))
    maxNum = max(maxNum, ans)
    minNum = min(minNum, ans)

print(maxNum)
print(minNum)
