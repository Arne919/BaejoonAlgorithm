import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 트리 입력
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 서브트리 크기 저장 배열
subtree = [0] * (N+1)

# DFS를 통한 서브트리 크기 계산
def dfs(node, parent):
    subtree[node] = 1  # 자기 자신 포함
    for nxt in graph[node]:
        if nxt != parent:
            dfs(nxt, node)
            subtree[node] += subtree[nxt]

dfs(R, -1)

# 쿼리 처리
for _ in range(Q):
    u = int(input())
    print(subtree[u])
