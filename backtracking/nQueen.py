def nQueen(board, N):
    if N == 0:
        return True
    for i in range(len(board)):
        for j in range(len(board[0])):
            if isAttacked(board, i, j):
                continue
            board[i][j] = 1
            if nQueen(board, N-1):
                return True
            board[i][j] = 0

    return False


def isAttacked(board, i, j):
    # check cols
    if any([val == 1 for val in board[i]]):
        return True

    # check for rows:
    if any([val == 1 for val in [row[j] for row in board]]):
        return True

    # diagonals
    for x in range(len(board)):
        for y in range(len(board[0])):
            if i+j == x+y and board[x][y] == 1:
                return True

    for x in range(len(board)):
        for y in range(len(board[0])):
            if i-j == x-y and board[x][y] == 1:
                return True
    return False


board = [[0 for _ in range(4)] for _ in range(4)]
r = nQueen(board, 4)
print(1)
