import sys

input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    px, py = find(x), find(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py


n, m = map(int, input().split())
parent = [x for x in range(n)]
ans = 0
for count in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        ans = count + 1
        break
    else:
        union(a, b)
print(ans)
