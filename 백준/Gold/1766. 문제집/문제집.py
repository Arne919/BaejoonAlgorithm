import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

# 1. indegree 0인 문제(가장 쉬운 문제들)를 pq에 넣기
pq = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

result = []

# 2. 우선순위 큐 기반 topological sort
while pq:
    now = heapq.heappop(pq)
    result.append(now)
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(pq, nxt)

# 3. 출력
print(*result)
