import sys

input = sys.stdin.readline

parent = dict()
network = dict()


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    px, py = find(x), find(y)
    if px != py:
        # parent[py] = px
        # network[px] += network[py]
        npx, npy = network[px], network[py]
        if npx >= npy:
            parent[py] = px
            network[px] += network[py]
        else:
            parent[px] = py
            network[py] += network[px]


t = int(input())

for _ in range(t):
    f = int(input())
    parent.clear()
    network.clear()
    for _ in range(f):
        a, b = input().split()

        if a not in parent:
            parent[a] = a
            network[a] = 1
        if b not in parent:
            parent[b] = b
            network[b] = 1

        union(a, b)
        print(network[find(parent[a])])
