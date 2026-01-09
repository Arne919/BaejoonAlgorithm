from collections import deque

N = int(input())
K = int(input())

# 보드 (0: 빈칸, 1: 사과)
board = [[0] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 1

L = int(input())
turns = {}
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C

# 방향: 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque()
snake.append((0, 0))  # 시작 위치
direction = 0
time = 0
x, y = 0, 0

while True:
    time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽 충돌
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        break

    # 자기 몸 충돌
    if (nx, ny) in snake:
        break

    snake.appendleft((nx, ny))

    if board[nx][ny] == 1:  # 사과
        board[nx][ny] = 0
    else:  # 사과 없으면 꼬리 제거
        snake.pop()

    x, y = nx, ny

    # 방향 전환
    if time in turns:
        if turns[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)
