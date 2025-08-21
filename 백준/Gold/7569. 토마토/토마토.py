import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())  # 가로, 세로, 높이

box = [[[0]*M for _ in range(N)] for _ in range(H)]
q = deque()
unripe = 0  # 익지 않은 토마토 개수

for h in range(H):
    for y in range(N):
        row = list(map(int, input().split()))
        box[h][y] = row
        for x, v in enumerate(row):
            if v == 1:
                q.append((h, y, x))
            elif v == 0:
                unripe += 1

# 처음부터 모두 익음
if unripe == 0:
    print(0)
    sys.exit(0)

# 6방향 (위/아래/앞/뒤/좌/우)
dirs = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

# 날짜 기록 배열
days = [[[-1]*M for _ in range(N)] for _ in range(H)]
for h, y, x in q:
    days[h][y][x] = 0

max_day = 0

while q:
    ch, cy, cx = q.popleft()
    for dh, dy, dx in dirs:
        nh, ny, nx = ch + dh, cy + dy, cx + dx
        if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
            if box[nh][ny][nx] == 0:  # 아직 안 익은 토마토만
                box[nh][ny][nx] = 1
                unripe -= 1
                days[nh][ny][nx] = days[ch][cy][cx] + 1
                max_day = max(max_day, days[nh][ny][nx])
                q.append((nh, ny, nx))

# 결과
print(-1 if unripe > 0 else max_day)
