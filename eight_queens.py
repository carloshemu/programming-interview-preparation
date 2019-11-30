"""
EIGHT QUEENS PUZZLE
Placing eight chess queens on an 8x8 chessboard so that no two queens threaten each other; thus, a solution requires
that no two queens share the same row, column, or diagonal
"""


"""
Sample solution 1: the recursive way
"""
def check(A, row, col):
    for r in range(row):
        if A[r] == col or r - A[r] == row - A[row] or r + A[r] == row + A[row]:  # Check same column, diagonal and anti-diagonal
            return False
    return True


def queen(A, row=0):
    if row == len(A):
        print(A)
    else:
        for col in range(len(A)):
            A[row] = col
            if check(A, row, col):
                queen(A, row + 1)

# queen([None] * 4)


"""
Sample solution 2: generator with yield
"""
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos, )
            else:
                for result in queens(num, state + (pos, )):
                    yield (pos, ) + result


# print(list((queens(4))))