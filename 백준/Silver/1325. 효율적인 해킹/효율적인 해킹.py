import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# A B: A가 B를 신뢰 → B를 해킹하면 A도 해킹 가능 → B -> A (역방향)
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

visited = [0] * (n + 1)

def bfs(s: int) -> int:
    mark = s                 # 시작점 고유 라벨
    dq = deque([s])
    visited[s] = mark
    cnt = 1                  # s 포함
    g = graph; vis = visited
    popleft = dq.popleft; append = dq.append

    while dq:
        u = popleft()
        for v in g[u]:
            if vis[v] != mark:
                vis[v] = mark
                append(v)
                cnt += 1
    return cnt

best = 0
ans = []
for i in range(1, n + 1):
    c = bfs(i)
    if c > best:
        best = c
        ans = [i]
    elif c == best:
        ans.append(i)

print(*ans)
