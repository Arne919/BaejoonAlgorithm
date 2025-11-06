import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def move(board, direction):
    # 0: up, 1: down, 2: left, 3: right
    new_board = [row[:] for row in board]

    if direction == 0:  # up
        for c in range(N):
            line = [new_board[r][c] for r in range(N) if new_board[r][c] != 0]
            merged = []
            i = 0
            while i < len(line):
                if i+1 < len(line) and line[i] == line[i+1]:
                    merged.append(line[i]*2)
                    i += 2
                else:
                    merged.append(line[i])
                    i += 1
            for r in range(N):
                new_board[r][c] = merged[r] if r < len(merged) else 0

    elif direction == 1:  # down
        for c in range(N):
            line = [new_board[r][c] for r in range(N-1, -1, -1) if new_board[r][c] != 0]
            merged = []
            i = 0
            while i < len(line):
                if i+1 < len(line) and line[i] == line[i+1]:
                    merged.append(line[i]*2)
                    i += 2
                else:
                    merged.append(line[i])
                    i += 1
            for r in range(N-1, -1, -1):
                new_board[r][c] = merged[N-1-r] if N-1-r < len(merged) else 0

    elif direction == 2:  # left
        for r in range(N):
            line = [new_board[r][c] for c in range(N) if new_board[r][c] != 0]
            merged = []
            i = 0
            while i < len(line):
                if i+1 < len(line) and line[i] == line[i+1]:
                    merged.append(line[i]*2)
                    i += 2
                else:
                    merged.append(line[i])
                    i += 1
            for c in range(N):
                new_board[r][c] = merged[c] if c < len(merged) else 0

    else:  # right
        for r in range(N):
            line = [new_board[r][c] for c in range(N-1, -1, -1) if new_board[r][c] != 0]
            merged = []
            i = 0
            while i < len(line):
                if i+1 < len(line) and line[i] == line[i+1]:
                    merged.append(line[i]*2)
                    i += 2
                else:
                    merged.append(line[i])
                    i += 1
            for c in range(N-1, -1, -1):
                new_board[r][c] = merged[N-1-c] if N-1-c < len(merged) else 0

    return new_board

answer = 0

def dfs(board, depth):
    global answer
    if depth == 5:
        answer = max(answer, max(max(row) for row in board))
        return
    
    for d in range(4):
        next_board = move(board, d)
        dfs(next_board, depth + 1)

dfs(board, 0)
print(answer)
