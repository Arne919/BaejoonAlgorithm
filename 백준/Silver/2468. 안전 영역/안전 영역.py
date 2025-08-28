import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
grid = [list(map(int, input().split())) for _ in range(N)]

max_h = max(max(row) for row in grid)
ans = 0

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

for h in range(0, max_h):  # h == max_h이면 전부 잠기므로 볼 필요 없음
    visited = [[False]*N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if grid[i][j] > h and not visited[i][j]:
                cnt += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and grid[nx][ny] > h:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    ans = max(ans, cnt)

print(ans if ans > 0 else 1)  # 모든 높이가 같아도 h=0에서 최소 1개 영역
