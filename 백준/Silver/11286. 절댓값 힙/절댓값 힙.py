import sys, heapq
input = sys.stdin.readline

N = int(input())
heap = []
out = []

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))  # (절댓값, 원래값)으로 정렬 → 절댓값 같으면 더 작은 수 우선
    else:
        out.append(str(heapq.heappop(heap)[1] if heap else 0))

sys.stdout.write('\n'.join(out))
