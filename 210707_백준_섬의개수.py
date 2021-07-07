import sys

sys.setrecursionlimit(int(1e6))
d = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]


def DFS(y, x, visited, board, num):
    land = board[y][x]
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        # 바깥으로 안나가고, 다음이 땅이고, 해당 지역을 카운트하지 않았다면
        if (
            0 <= ny < h
            and 0 <= nx < w
            and board[ny][nx] == land
            and visited[ny][nx] == 0
        ):
            visited[ny][nx] = num
            DFS(ny, nx, visited, board, num)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]
    num = 0
    for i in range(h):
        for j in range(w):
            # 바다거나, 이미 방문했다면 다음
            if board[i][j] == 0 or visited[i][j] != 0:
                continue

            # 땅이고, 방문하지 않은 경우 탐색
            DFS(i, j, visited, board, num + 1)
            num += 1
    print(num)
