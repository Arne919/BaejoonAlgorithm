import sys, heapq
input = sys.stdin.readline
INF = int(1e15)

def dijkstra(start, graph, n):
    dist = [INF] * (n+1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u]:
            continue
        for w, v in graph[u]:
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    return dist

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

dist1 = dijkstra(1, graph, N)
distv1 = dijkstra(v1, graph, N)
distv2 = dijkstra(v2, graph, N)

# 두 가지 경우
path1 = dist1[v1] + distv1[v2] + distv2[N]
path2 = dist1[v2] + distv2[v1] + distv1[N]

answer = min(path1, path2)
print(answer if answer < INF else -1)
