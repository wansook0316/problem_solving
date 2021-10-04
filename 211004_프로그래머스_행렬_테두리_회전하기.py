def change(board, y, x, number) -> int:
    tempNumber = board[y][x]
    board[y][x] = number
    return tempNumber


def rotate(board, sy, sx, ey, ex) -> int:

    minNumber = int(1e6)
    prevNumber = board[sy][sx]

    y, x = sy, sx
    for j in range(sx + 1, ex + 1):
        x = j
        minNumber = min(minNumber, prevNumber)
        prevNumber = change(board, y, x, prevNumber)

    for i in range(sy + 1, ey + 1):
        y = i
        minNumber = min(minNumber, prevNumber)
        prevNumber = change(board, y, x, prevNumber)

    for j in range(ex - 1, sx - 1, -1):
        x = j
        minNumber = min(minNumber, prevNumber)
        prevNumber = change(board, y, x, prevNumber)

    for i in range(ey - 1, sy - 1, -1):
        y = i
        minNumber = min(minNumber, prevNumber)
        prevNumber = change(board, y, x, prevNumber)

    return minNumber


def solution(rows, cols, queries):
    answer = []
    board = [[row * cols + col + 1 for col in range(cols)] for row in range(rows)]

    for sy, sx, ey, ex in queries:
        answer.append(rotate(board, sy - 1, sx - 1, ey - 1, ex - 1))

    return answer
