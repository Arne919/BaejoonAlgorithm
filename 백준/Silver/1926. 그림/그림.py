import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

# 상하좌우 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    area = 1  # 그림 넓이 (1의 개수)

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and paper[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    area += 1
    return area

count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            count += 1
            max_area = max(max_area, bfs(i, j))

print(count)
print(max_area)
