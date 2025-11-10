import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
bags = []

for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))

for _ in range(K):
    bags.append(int(input()))

# 보석: 무게 기준 정렬
jewels.sort()
# 가방: 수용 무게 기준 정렬
bags.sort()

max_heap = []  # 담을 수 있는 보석 중 가격 큰 것 선택 (최대 힙)
result = 0
idx = 0

for bag in bags:
    # 현재 가방에 넣을 수 있는 보석들 힙에 push
    while idx < N and jewels[idx][0] <= bag:
        heapq.heappush(max_heap, -jewels[idx][1])  # 최대 힙 위해 음수 저장
        idx += 1
    
    # 가능한 보석 중 가장 비싼 것 선택
    if max_heap:
        result += -heapq.heappop(max_heap)

print(result)
