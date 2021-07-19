import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
operator_list = input().split()
ans = ""
count = 0
top = 9
for operator in operator_list:
    if operator == ">":
        for i in range(top - count, top + 1):
            ans += str(i)
        top = top - count - 1
        count = 0
    else:
        count += 1
for i in range(top - count, top + 1):
    ans += str(i)
top = top - count - 1
count = 0
print(ans)

ans = ""
count = 0
top = 0
for operator in operator_list:
    if operator == "<":
        for i in range(top + count, top - 1, -1):
            ans += str(i)
        top = top + count + 1
        count = 0
    else:
        count += 1
for i in range(top + count, top - 1, -1):
    ans += str(i)
top = top + count + 1
count = 0
print(ans)