import sys
import heapq

input = sys.stdin.readline
N = int(input())

max_heap = []

for _ in range(N):
    x = int(input())

    if x > 0:
        heapq.heappush(max_heap, -x)  # 음수로 넣어서 최대 힙처럼 사용
    else:
        if max_heap:
            print(-heapq.heappop(max_heap))  # 꺼낼 때 다시 음수 부호 제거
        else:
            print(0)
