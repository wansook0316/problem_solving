import sys

n = int(input())
company_dict = dict()

for _ in range(n):
    name, action = input().split()

    if name not in company_dict:
        company_dict[name] = False

    if action == "enter":
        company_dict[name] = True
    elif action == "leave":
        company_dict[name] = False

ans = []
for name, state in company_dict.items():
    if state:
        ans.append(name)
ans = sorted(ans, reverse=True)
for name in ans:
    print(name)