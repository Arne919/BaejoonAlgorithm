import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

grid = []
for _ in range(N):
    # 입력이 공백 있는/없는 두 형태가 섞여 나오는 경우가 있어서 통일 처리
    row = list(map(int, input().split()))
    if len(row) == 1 and M > 1:  # "0001010" 같은 형식 방지용
        row = list(map(int, list(str(row[0]))))
    grid.append(row)

empties = []
viruses = []
for r in range(N):
    for c in range(M):
        if grid[r][c] == 0:
            empties.append((r, c))
        elif grid[r][c] == 2:
            viruses.append((r, c))

start_safe = len(empties) - 3  # 벽 3개를 세우면 기본적으로 3칸은 줄어듦
best = 0

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

for (r1, c1), (r2, c2), (r3, c3) in combinations(empties, 3):
    # 벽 세우기
    grid[r1][c1] = grid[r2][c2] = grid[r3][c3] = 1

    # BFS로 감염 수 계산
    q = deque(viruses)
    visited = [[False]*M for _ in range(N)]
    for vr, vc in viruses:
        visited[vr][vc] = True

    infected = 0
    # 가지치기 한계
    limit = start_safe - best  # 이만큼 이상 감염되면 갱신 불가능

    stop = False
    while q and not stop:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if grid[nr][nc] == 0:   # 빈 칸만 감염 가능
                    visited[nr][nc] = True
                    infected += 1
                    if infected >= limit:
                        stop = True
                        break
                    q.append((nr, nc))
                elif grid[nr][nc] == 2:
                    visited[nr][nc] = True
                    q.append((nr, nc))

    if not stop:
        # 안전영역 = 남은 빈칸
        safe = start_safe - infected
        if safe > best:
            best = safe

    # 벽 원복
    grid[r1][c1] = grid[r2][c2] = grid[r3][c3] = 0

print(best)
