from itertools import combinations
import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    summations = list(map(sum, combinations(cards, 3)))
    print(max(filter(lambda x: x <= m, summations)))


if __name__ == "__main__":
    main()

# 10 500
# 93 181 245 214 315 36 185 138 216 295