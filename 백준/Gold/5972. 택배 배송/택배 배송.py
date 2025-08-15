import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

INF = 10**18
dist = [INF] * (N + 1)
dist[1] = 0

hq = [(0, 1)]  # (현재까지 비용, 노드)
while hq:
    cost, u = heapq.heappop(hq)
    if cost != dist[u]:
        continue
    for v, w in adj[u]:
        nd = cost + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(hq, (nd, v))

print(dist[N])
