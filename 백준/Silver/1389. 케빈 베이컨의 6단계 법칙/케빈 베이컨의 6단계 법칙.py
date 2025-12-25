from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = deque([start])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    return sum(dist[1:])  # 자기 자신(0 포함해도 무방)

answer = 1
min_sum = bfs(1)

for i in range(2, N + 1):
    s = bfs(i)
    if s < min_sum:
        min_sum = s
        answer = i

print(answer)
