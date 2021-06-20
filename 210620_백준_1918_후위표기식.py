import sys

input = sys.stdin.readline

string = input()
# string = "A*((B+C/D-E)*F)"
stack = []
ans = ""


def operationPriority(op):
    if op in "+-":
        return "+-*/"
    else:
        return "*/"


for c in string:
    # 만약 "("이면 stack에 넣는다.
    if c == "(":
        stack.append(c)
    # 만약 ")"이면 여는 괄호가 나올 때까지 stack을 뒤지며 중간과정을 ans에 추가한다.
    elif c == ")":
        while stack:
            if stack[-1] == "(":
                stack.pop()
                break
            ans += stack.pop()
    # 만약 알파벳이면 ans 에 추가한다.
    elif c.isalpha():
        ans += c
    # 만약 +-*/이면 각각의 우선 순위보다 같거나 높은 요소를 ans에 붙인다.
    # 그렇지 않은 요소가 발견되거나
    # +-*/가 아닌 경우 탈출한다.
    elif c in "+-*/":
        opPriority = operationPriority(c)
        while stack:
            if stack[-1] not in opPriority:
                break
            ans += stack.pop()
        stack.append(c)
while stack:
    ans += stack.pop()

print(ans)


# 앞에서 부터 순차적으로 본다

# 만약 "("이면 stack에 넣는다.

# 만약 ")"이면 여는 괄호가 나올 때까지 stack을 뒤지며 중간과정을 ans에 추가한다.

# 만약 알파벳이면 ans 에 추가한다.

# 만약 +-*/이면 각각의 우선 순위보다 같거나 높은 요소를 ans에 붙인다.
# 그렇지 않은 요소가 발견되거나
# +-*/가 아닌 경우 탈출한다.

# 다 봤으면 stack에 남은 원소를 뒤에다가 모두 붙인다.