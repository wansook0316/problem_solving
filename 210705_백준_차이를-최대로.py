import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))


def calculate(array):
    ret = 0
    for a, b in zip(array[:-1], array[1:]):
        ret += abs(a - b)
    return ret


max_number = 0
possible = set(permutations(a, len(a)))

for cand in possible:
    max_number = max(max_number, calculate(cand))
print(max_number)