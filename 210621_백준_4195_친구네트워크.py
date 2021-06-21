import sys

input = sys.stdin.readline
parent = []


def find(x):
    if parent[x][0] == x:
        return x
    else:
        parent[x][0] = find(parent[x][0])
        return parent[x][0]


def union(x, y):
    px, py = find(x), find(y)
    if px < py:
        parent[py][0] = px
        parent[px][1] += parent[py][1]
    else:
        parent[px][0] = py
        parent[py][1] += parent[px][1]


T = int(input())

for _ in range(T):
    f = int(input())
    name_dict = dict()
    num = 0
    parent = []
    for _ in range(f):
        a, b = input().split()
        if a not in name_dict:
            name_dict[a] = num
            parent.append([num, 1])
            num += 1
        if b not in name_dict:
            name_dict[b] = num
            parent.append([num, 1])
            num += 1

        if find(name_dict[a]) != find(name_dict[b]):
            union(name_dict[a], name_dict[b])

        print(parent[find(name_dict[a])][1])
