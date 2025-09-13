from collections import deque

N = int(input().strip())
grid = [list(input().strip()) for _ in range(N)]

# 4방향 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color, visited, board):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and board[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append((nx, ny))

def count_regions(board):
    visited = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, board[i][j], visited, board)
                count += 1
    return count

# 일반인
normal = count_regions(grid)

# 적록색약: R을 G로 바꿔버리기
rg_board = [['G' if c == 'R' else c for c in row] for row in grid]
color_blind = count_regions(rg_board)

print(normal, color_blind)
