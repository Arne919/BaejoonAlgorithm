import sys
from collections import deque

def main():
    input = sys.stdin.readline
    M, N = map(int, input().split())
    
    box = [list(map(int, input().split())) for _ in range(N)]
    q = deque()
    
    # 초기 익은 토마토(1)를 큐에 넣음
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append((i, j))
    
    # BFS (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < M:
                if box[ny][nx] == 0:  # 안 익은 토마토
                    box[ny][nx] = box[y][x] + 1  # 날짜 기록
                    q.append((ny, nx))
    
    # 결과 계산
    result = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:  # 안 익은 토마토가 남아있음
                print(-1)
                return
            result = max(result, box[i][j])
    
    print(result - 1)  # 첫날(1)에서 시작했으므로 -1 보정

if __name__ == "__main__":
    main()
