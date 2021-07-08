# 앞에서 부터 가장 큰 녀석이 나올 때까지 지운다.
# 근데 지우는 개수가 초과되면그냥 넣어버려야 함

# 스택이 비어있다? -> 일단 집어 넣는다.
# 다음 요소를 봤는데 현재 ㄴtack의 top보다 크다.
# 그럼 그 큰 요소가 처음이 될만한 가치가 있음
# 스택에서 뺸다.
# 집어 넣는다.
# 뺀 개수 하나 줄인다.
# 만약 다 뺴버렸다.
# 그럼 뒤에 그냥 다 넣으면 답

n, k = map(int, input().split())
target = input()
stack = []
_k = k
for char in target:
    while stack and _k > 0 and stack[-1] < char:
        stack.pop()
        _k -= 1
    stack.append(char)

print("".join(stack)[: n - k])
