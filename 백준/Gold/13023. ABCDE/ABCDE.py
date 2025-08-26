import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False]*N
found = False

def dfs(u, depth):
    global found
    if found:  # 이미 찾았으면 더 탐색 X
        return
    if depth == 4:  # A-B-C-D-E로 4개의 간선 = 5명
        found = True
        return
    for v in g[u]:
        if not visited[v]:
            visited[v] = True
            dfs(v, depth+1)
            visited[v] = False
            if found:
                return

for i in range(N):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False
    if found:
        print(1)
        break
else:
    print(0)
