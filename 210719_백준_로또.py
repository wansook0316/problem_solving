import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    input_list = list(map(int, input().split()))
    if input_list[0] == 0:
        break
    k, s = input_list[0], input_list[1:]

    for combi in list(combinations(s, 6)):
        for c in combi:
            print(c, end=" ")
        print()
    print()