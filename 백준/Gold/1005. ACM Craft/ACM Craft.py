import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N+1)

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1

    W = int(input())

    # 위상정렬 + DP
    time = [0] * (N+1)
    q = deque()

    # 초기 시작 건물들 (선행 없음)
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            time[i] = D[i]

    while q:
        now = q.popleft()
        if now == W:
            break
        for nxt in graph[now]:
            indegree[nxt] -= 1
            time[nxt] = max(time[nxt], time[now] + D[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)

    print(time[W])
