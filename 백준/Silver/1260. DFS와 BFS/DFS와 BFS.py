import sys
from collections import deque

input = sys.stdin.readline

# 입력
N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

# 간선 정보
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정점 번호가 작은 것부터 방문해야 하므로 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS
visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)

dfs(V)
print()

# BFS
visited = [False] * (N + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

bfs(V)
