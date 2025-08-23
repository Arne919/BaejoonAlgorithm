import sys
import heapq

input = sys.stdin.readline
INF = 10**15

N = int(input())                # 도시 수
M = int(input())                # 버스(간선) 수

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(start, end):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]  # (현재까지 비용, 노드)

    while pq:
        cost, u = heapq.heappop(pq)
        # 이미 더 싼 경로를 처리했으면 무시
        if cost > dist[u]:
            continue
        # 목적지면 종료 (최소 비용 보장)
        if u == end:
            return cost
        # 인접 정점 완화
        for v, w in graph[u]:
            nc = cost + w
            if nc < dist[v]:
                dist[v] = nc
                heapq.heappush(pq, (nc, v))
    return dist[end]

print(dijkstra(start, end))
