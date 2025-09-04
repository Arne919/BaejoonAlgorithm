import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
board = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def cut(x: int, y: int, n: int):
    global white, blue
    first = board[x][y]
    same = True
    for i in range(x, x + n):
        if not same: break
        for j in range(y, y + n):
            if board[i][j] != first:
                same = False
                break

    if same:
        if first == 0:
            white += 1
        else:
            blue += 1
        return

    h = n // 2
    cut(x, y, h)
    cut(x, y + h, h)
    cut(x + h, y, h)
    cut(x + h, y + h, h)

cut(0, 0, N)
print(white)
print(blue)
