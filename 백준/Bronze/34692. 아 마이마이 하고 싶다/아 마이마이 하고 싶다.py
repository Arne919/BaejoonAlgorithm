import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
times = list(map(int, input().split()))

# 초기 기기 상태: 모두 0
pq = [0] * M
heapq.heapify(pq)

# N명의 사람들 처리
for t in times:
    cur = heapq.heappop(pq)
    heapq.heappush(pq, cur + t)

# 코이의 최소 대기 시간
min_wait = pq[0]

# 비교
if min_wait <= K:
    print("WAIT")
else:
    print("GO")
