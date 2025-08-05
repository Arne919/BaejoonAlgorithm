import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for adj in graph:
    adj.sort()

visited = [0] * (N + 1)  # 방문 순서 저장 (0이면 아직 방문하지 않음)
order = 1  # 방문 순서 횟수

def dfs(node):
    global order
    visited[node] = order
    for next_node in graph[node]:
        if visited[next_node] == 0:
            order += 1
            dfs(next_node)
            
dfs(R)

for i in range(1, N + 1):
    print(visited[i])
