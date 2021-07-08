from pprint import pprint


def DFS(cy, cx, iy, ix, fy, fx, board):
    global visited
    if cy == fy and cx == fx:
        return 1

    for dy, dx in d:
        ny, nx = cy + dy, cx + dx
        if iy <= ny <= fy and ix <= nx <= fx:
            if visited[ny][nx] == 0:
                visited[ny][nx] = DFS(ny, nx, iy, ix, fy, fx, board)
            visited[cy][cx] += visited[ny][nx]
    return visited[cy][cx]


n, m, k = map(int, input().split())
board = [[(i * m + 1) + j for j in range(m)] for i in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
d = [[1, 0], [0, 1]]
answer = 0

if k == 0:
    DFS(0, 0, 0, 0, n - 1, m - 1, board)
    answer = visited[0][0]
else:
    k_i, k_j = divmod(k - 1, m)
    DFS(0, 0, 0, 0, k_i, k_j, board)
    visited[k_i][k_j] = 0
    DFS(k_i, k_j, k_i, k_j, n - 1, m - 1, board)
    answer = visited[0][0] * visited[k_i][k_j]

print(answer)
