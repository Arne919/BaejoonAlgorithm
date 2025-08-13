import sys
import heapq
input = sys.stdin.readline

INF = 10**9
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [INF] * (V+1)
dist[K] = 0
pq = [(0, K)]

while pq:
    d, now = heapq.heappop(pq)
    if dist[now] < d:
        continue
    for nxt, cost in graph[now]:
        nd = d + cost
        if nd < dist[nxt]:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

for i in range(1, V+1):
    print(dist[i] if dist[i] != INF else "INF")
