import sys
import heapq

input = sys.stdin.readline
N = int(input())
cards = [int(input()) for _ in range(N)]

if N == 1:
    print(0)
else:
    heapq.heapify(cards)
    ans = 0
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        s = a + b
        ans += s
        heapq.heappush(cards, s)
    print(ans)
