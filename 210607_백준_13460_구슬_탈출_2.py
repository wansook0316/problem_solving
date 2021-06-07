import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

tetromino = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],  # ㅜ
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # ㅗ
    [(0, 0), (1, 0), (2, 0), (1, 1)],  # ㅏ
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # ㅓ
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
]


def solve():
    for i in range(n):
        for j in range(m):
            find(i, j)


def find(y, x):
    global answer
    for i in range(len(tetromino)):
        result = 0
        for j in range(4):
            try:
                next_y = y+tetromino[i][j][0]
                next_x = x+tetromino[i][j][1]
                result += graph[next_y][next_x]
            except IndexError:
                continue
        answer = max(answer, result)


answer = 0
solve()
print(answer)