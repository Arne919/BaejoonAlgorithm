import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

parent = [0] * (N + 1)
parent[1] = -1  # 루트 표시

q = deque([1])
while q:
    u = q.popleft()
    for v in adj[u]:
        if parent[v] == 0:      # 아직 방문 안 했으면
            parent[v] = u
            q.append(v)

out = []
for i in range(2, N + 1):
    out.append(str(parent[i]))
print('\n'.join(out))
