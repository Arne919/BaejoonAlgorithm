import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, list(input().strip()))) for _ in range(N)]

# 거리 배열 (시작을 1로 카운트)
dist = [[0]*M for _ in range(N)]
dist[0][0] = 1

q = deque([(0, 0)])
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while q:
    x, y = q.popleft()
    if x == N-1 and y == M-1:
        print(dist[x][y])
        break
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and dist[nx][ny] == 0:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
