from collections import deque

N, M = map(int, input().split())

# next_position[i] = 사다리/뱀에 의해 이동할 위치 (없으면 자기 자신)
next_position = list(range(101))

for _ in range(N):
    x, y = map(int, input().split())
    next_position[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    next_position[u] = v

# BFS
visited = [False] * 101
queue = deque()
queue.append((1, 0))   # (현재 칸, 굴린 횟수)
visited[1] = True

while queue:
    pos, cnt = queue.popleft()

    # 목표 도달
    if pos == 100:
        print(cnt)
        break

    for dice in range(1, 7):
        nxt = pos + dice
        if nxt > 100:
            continue

        # 사다리/뱀 이동 처리
        nxt = next_position[nxt]

        if not visited[nxt]:
            visited[nxt] = True
            queue.append((nxt, cnt + 1))
