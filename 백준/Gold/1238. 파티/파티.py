import sys
import heapq

input = sys.stdin.readline
INF = 10**9

def dijkstra(start, graph, n):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def main():
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    rev_graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))       # a -> b
        rev_graph[b].append((a, t))   # reversed: b -> a becomes a -> b in rev graph (for paths to X)

    # X -> i (원래 그래프에서)
    dist_from_X = dijkstra(X, graph, N)
    # i -> X (원래 그래프에서) == X -> i in rev_graph
    dist_to_X = dijkstra(X, rev_graph, N)

    ans = 0
    for i in range(1, N+1):
        total = dist_to_X[i] + dist_from_X[i]
        if total > ans:
            ans = total

    print(ans)

if __name__ == "__main__":
    main()
