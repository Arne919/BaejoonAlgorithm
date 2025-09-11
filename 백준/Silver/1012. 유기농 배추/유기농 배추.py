import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 증가 (DFS 용)

def dfs(x, y, field, visited, M, N):
    visited[y][x] = True
    # 상하좌우 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if field[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx, ny, field, visited, M, N)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    # 2차원 밭 배열과 방문 배열 초기화
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    
    # 배추 위치 표시
    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1
    
    count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                dfs(x, y, field, visited, M, N)
                count += 1
    print(count)
