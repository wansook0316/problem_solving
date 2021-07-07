import sys
from pprint import pprint

sys.setrecursionlimit(int(1e6))


def find(x):
    if parent[x][0] == x:
        return parent[x]
    else:
        node_num, memory = find(parent[x][0])
        parent[x][0] = node_num
        return parent[x]


def union(x, y):
    [a_num, a_memory], [b_num, b_memory] = find(x), find(y)
    if a_num != b_num:
        parent[b_num][0] = parent[a_num][0]
        parent[b_num][1] = a_memory + parent[b_num][1]


def calculate(x, y):
    a, b = find(x)[1], find(y)[1]
    if a[0] != b[0]:
        return -1
    bound = 0
    for i, (p, r) in enumerate(zip(a, b)):
        if p == r:
            bound = i
    return len(a[bound + 1 :]) + len(b[bound + 1 :])


n = int(input())
parent = [[x, [x]] for x in range(n + 1)]
a, b = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    union(x, y)

print(calculate(a, b))
# answer = -1

# 18
# 7 11
# 15
# 1 2
# 1 3
# 1 4
# 2 5
# 2 6
# 4 10
# 6 7
# 6 8
# 6 9
# 10 11
# 10 12
# 12 13
# 14 15
# 15 16
# 17 18
