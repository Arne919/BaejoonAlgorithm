import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# 시작과 끝이 같은 경우
if N == 1 and M == 1:
    print(1)
    sys.exit(0)

# 방문 배열: 각 상태(벽 안 부숨 / 부숨)별로 N*M 크기의 1차원 배열
size = N * M
vis0 = bytearray(size)  # 아직 벽을 부수지 않은 상태에서 방문
vis1 = bytearray(size)  # 이미 벽을 한 번 부순 상태에서 방문

def idx(r, c):
    return r * M + c

dq = deque()
dq.append((0, 0, 0))  # r, c, broken(0/1)
vis0[idx(0, 0)] = 1

steps = 1  # 시작 칸 포함
target = (N - 1, M - 1)
DIRS = ((1,0), (-1,0), (0,1), (0,-1))

while dq:
    steps += 1
    for _ in range(len(dq)):
        r, c, broke = dq.popleft()
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if (nr, nc) == target:
                print(steps)
                sys.exit(0)

            nlinear = idx(nr, nc)
            cell = grid[nr][nc]

            if cell == '0':
                if broke == 0:
                    if not vis0[nlinear]:
                        vis0[nlinear] = 1
                        dq.append((nr, nc, 0))
                else:
                    if not vis1[nlinear]:
                        vis1[nlinear] = 1
                        dq.append((nr, nc, 1))
            else:  # cell == '1'
                if broke == 0 and not vis1[nlinear]:
                    # 이 벽을 부수고 이동
                    vis1[nlinear] = 1
                    dq.append((nr, nc, 1))

print(-1)
