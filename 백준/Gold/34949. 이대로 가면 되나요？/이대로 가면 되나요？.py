import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 역방향 그래프
rev = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    rev[A[i - 1]].append(i)

dist = [-1] * (N + 1)
dist[N] = 0

q = deque([N])

while q:
    cur = q.popleft()
    for nxt in rev[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

for i in range(1, N + 1):
    print(dist[i])
