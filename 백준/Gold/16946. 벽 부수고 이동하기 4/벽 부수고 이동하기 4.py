import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

group = [[-1] * M for _ in range(N)]
group_size = []
group_id = 0

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# Step 1: 0 영역 BFS로 그룹 번호 부여
for i in range(N):
    for j in range(M):
        if grid[i][j] == '0' and group[i][j] == -1:
            q = deque()
            q.append((i, j))
            group[i][j] = group_id
            size = 1

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < N and 0 <= ny < M:
                        if grid[nx][ny] == '0' and group[nx][ny] == -1:
                            group[nx][ny] = group_id
                            q.append((nx, ny))
                            size += 1

            group_size.append(size)
            group_id += 1

# Step 2: 벽일 때 주변 그룹 크기 합산
result = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == '1':
            seen = set()
            cnt = 1  # 벽이 없어져서 자기 자신 포함
            for d in range(4):
                nx, ny = i + dx[d], j + dy[d]
                if 0 <= nx < N and 0 <= ny < M:
                    gid = group[nx][ny]
                    if gid != -1 and gid not in seen:
                        seen.add(gid)
                        cnt += group_size[gid]
            result[i][j] = cnt % 10
        else:
            result[i][j] = 0

# 출력
for i in range(N):
    print("".join(map(str, result[i])))
