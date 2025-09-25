from collections import deque
import sys
input = sys.stdin.readline

# 방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited, iceberg, N, M):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if iceberg[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def melt(iceberg, N, M):
    # 줄어드는 높이 계산용 임시 배열
    melt_amount = [[0]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0:
                cnt = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < N and 0 <= nj < M and iceberg[ni][nj] == 0:
                        cnt += 1
                melt_amount[i][j] = cnt
    
    # 실제 높이 감소 적용
    for i in range(N):
        for j in range(M):
            iceberg[i][j] = max(0, iceberg[i][j] - melt_amount[i][j])

def count_components(iceberg, N, M):
    visited = [[False]*M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited, iceberg, N, M)
                count += 1
    return count

def main():
    N, M = map(int, input().split())
    iceberg = [list(map(int, input().split())) for _ in range(N)]
    
    year = 0
    while True:
        comp = count_components(iceberg, N, M)
        if comp == 0:
            print(0)
            return
        if comp >= 2:
            print(year)
            return
        
        melt(iceberg, N, M)
        year += 1

if __name__ == "__main__":
    main()
