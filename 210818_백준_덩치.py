import sys

input = sys.stdin.readline


def main():
    n = int(input())
    guys = [list(map(int, input().split())) for _ in range(n)]
    ret = []
    for i in range(n):
        rank = 1
        for j in range(n):
            if i == j:
                continue
            if guys[i][0] < guys[j][0] and guys[i][1] < guys[j][1]:
                rank += 1
        ret.append(rank)
    print(" ".join(list(map(str, ret))))


if __name__ == "__main__":
    main()