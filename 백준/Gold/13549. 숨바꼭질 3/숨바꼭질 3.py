import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

MAX = 100000
INF = 10**9
dist = [INF] * (MAX + 1)

dq = deque([N])
dist[N] = 0

while dq:
    x = dq.popleft()
    if x == K:
        # 최단 시간이 확정되었어도, 0비용 이동이 남아 있을 수 있지만
        # dist[K]가 더 줄어들 수는 없음.
        pass

    # 0초 순간이동
    nx = x * 2
    if nx <= MAX and dist[nx] > dist[x]:
        dist[nx] = dist[x]
        dq.appendleft(nx)

    # 1초 걷기
    for nx in (x - 1, x + 1):
        if 0 <= nx <= MAX and dist[nx] > dist[x] + 1:
            dist[nx] = dist[x] + 1
            dq.append(nx)

print(dist[K])
