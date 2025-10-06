import sys
sys.setrecursionlimit(10000)  # 재귀 깊이 제한 증가

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

# 방향 벡터 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 방문한 곳은 0으로 변경
    graph[x][y] = 0
    count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 확인
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            count += dfs(nx, ny)
    return count

result = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(dfs(i, j))

# 결과 출력
result.sort()
print(len(result))
for r in result:
    print(r)
