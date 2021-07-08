A, B = input().split()

min_diff = 100
for i in range(len(B) - len(A) + 1):
    diff = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            diff += 1
    min_diff = min(min_diff, diff)

print(min_diff)
