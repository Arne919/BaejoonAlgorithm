import sys
import heapq

# 최소 신장 그래프
input = sys.stdin.readline
n = int(input())
self_cost = [int(input()) for _ in range(n)]  # 직접 우물을 파는 비용
cost = [list(map(int, input().split())) for _ in range(n)]  # 다른 논으로부터 물을 끌어오는 비용
heap = [(self_cost[i], i) for i in range(n)]  # 직접 우물을 파는 경우에 대해 (비용, 정점) 순으로 모두 추가한다.
heapq.heapify(heap)  # list인 heap을 heapq로 변경한다.

visited = [0] * n  # 해당 논에 물을 댔는지 관리
cnt = 0  # 물을 댄 논 개수
result = 0  # 최종 비용
while heap:
    if cnt == n:
        break
    c, v = heapq.heappop(heap)  # 힙에 있는 최소 비용, 논 pop
    if visited[v]:  # 이미 물을 댄 논이면 pass
        continue
    visited[v] = 1
    cnt += 1
    result += c
    for i in range(n):  # 이번 턴에 물을 댄 논과 연결된 논들을 heap에 추가
        heapq.heappush(heap, (cost[v][i], i))

print(result)