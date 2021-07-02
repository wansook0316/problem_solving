import sys

input = sys.stdin.readline

n, m = map(int, input().split())

name_dict = dict()
answer = []
for _ in range(n + m):
    name = input().rstrip()
    if name not in name_dict:
        name_dict[name] = 0
    name_dict[name] += 1
    if name_dict[name] == 2:
        answer.append(name)
answer.sort()
print(len(answer))
for a in answer:
    print(a)