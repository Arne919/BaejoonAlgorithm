import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

# 각 행, 열, 박스에 숫자가 사용되었는지 기록
row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
box = [[False]*10 for _ in range(9)]

zeros = []

# 초기 상태 기록
for i in range(9):
    for j in range(9):
        n = board[i][j]
        if n == 0:
            zeros.append((i, j))
        else:
            row[i][n] = True
            col[j][n] = True
            box[(i//3)*3 + (j//3)][n] = True


def solve(idx):
    if idx == len(zeros):
        for r in board:
            print(*r)
        exit(0)

    r, c = zeros[idx]
    b = (r//3)*3 + (c//3)

    for num in range(1, 10):
        if not row[r][num] and not col[c][num] and not box[b][num]:
            board[r][c] = num
            row[r][num] = col[c][num] = box[b][num] = True

            solve(idx + 1)

            board[r][c] = 0
            row[r][num] = col[c][num] = box[b][num] = False


solve(0)
