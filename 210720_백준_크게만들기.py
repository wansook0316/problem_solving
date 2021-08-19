# 일단 앞에 가장 큰 숫자가 와야 함
# 아래로 내려가는 모양새가 되되, 치운 문자의 개수가 K가 된 경우 이후를 그냥 붙여버림

# 4

# 7 7 5 8 4 1

# 2
# 9 4

# stack이 비지 않은 경우, 가장 끝 원소가 현재 원소보다 작을 경우, removed count가 아직 보다 작은 경우

n, k = map(int, input().split())
number = input()

removed = 0
stack = []

for now in number:
    while stack and stack[-1] < now and removed < k:
        stack.pop()
        removed += 1
    stack.append(now)

print("".join(stack[: n - k]))
