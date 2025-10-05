from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

fire_time = [[INF] * C for _ in range(R)]
jihun_time = [[-1] * C for _ in range(R)]

q_fire = deque()
q_jihun = deque()

# 초기 세팅
for i in range(R):
    for j in range(C):
        if maze[i][j] == "F":
            q_fire.append((i, j))
            fire_time[i][j] = 0
        elif maze[i][j] == "J":
            start = (i, j)
            jihun_time[i][j] = 0

# 불 BFS
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q_fire:
    x, y = q_fire.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if maze[nx][ny] != "#" and fire_time[nx][ny] == INF:
                fire_time[nx][ny] = fire_time[x][y] + 1
                q_fire.append((nx, ny))

# 지훈 BFS
q_jihun.append(start)

while q_jihun:
    x, y = q_jihun.popleft()

    # 가장자리 도달 → 탈출
    if x == 0 or x == R-1 or y == 0 or y == C-1:
        print(jihun_time[x][y] + 1)
        sys.exit(0)

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if maze[nx][ny] == "." and jihun_time[nx][ny] == -1:
                # 지훈이가 불보다 먼저 가야 함
                if jihun_time[x][y] + 1 < fire_time[nx][ny]:
                    jihun_time[nx][ny] = jihun_time[x][y] + 1
                    q_jihun.append((nx, ny))

# 탈출 실패
print("IMPOSSIBLE")
