from collections import deque
import sys
input = sys.stdin.readline

# 나이트 이동 방향
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

T = int(input())

for _ in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    # 시작과 끝이 같으면 0
    if sx == ex and sy == ey:
        print(0)
        continue

    visited = [[-1] * l for _ in range(l)]
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1

                if nx == ex and ny == ey:
                    print(visited[nx][ny])
                    queue.clear()
                    break

                queue.append((nx, ny))
