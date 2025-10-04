import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = []
start = None

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
    for j, v in enumerate(row):
        if v == 2:
            start = (i, j)

# 거리 배열: -1 = 미방문(도달 불가 표시용)
dist = [[-1] * m for _ in range(n)]

# 원래 0인 칸은 출력 0으로 해야 하므로 dist에 특별 처리하지 않아도 출력 시 처리 가능
# BFS 시작 (목표 지점)
dq = deque()
si, sj = start
dist[si][sj] = 0
dq.append((si, sj))

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while dq:
    x, y = dq.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            # 갈 수 있는 땅(1)만 이동 가능. (2는 시작점으로 이미 처리)
            if grid[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                dq.append((nx, ny))

# 출력: 원래 0이면 0, 원래 1이면 dist (도달 불가하면 -1), 원래 2이면 0
out_lines = []
for i in range(n):
    row_out = []
    for j in range(m):
        if grid[i][j] == 0:
            row_out.append('0')
        else:
            # grid==1 혹은 2
            # dist는 시작(2)에 대해 0, 도달불가면 -1
            row_out.append(str(dist[i][j]))
    out_lines.append(' '.join(row_out))

print('\n'.join(out_lines))
