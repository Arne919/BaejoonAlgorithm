import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    last = list(map(int, input().split()))
    
    # 그래프 및 indegree 준비
    adj = [[False]*(n+1) for _ in range(n+1)]
    indeg = [0]*(n+1)
    
    # 1. 작년 순위를 기반으로 그래프 구축
    for i in range(n):
        for j in range(i+1, n):
            a = last[i]
            b = last[j]
            # a(작년 기준 더 높은 팀) → b(더 낮은 팀)
            adj[a][b] = True
            indeg[b] += 1
    
    # 2. 올해 뒤집힌 정보 반영 (간선 방향 swap)
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        # 간선 방향을 뒤집어야 한다.
        if adj[a][b]:
            adj[a][b] = False
            adj[b][a] = True
            indeg[b] -= 1
            indeg[a] += 1
        else:
            adj[b][a] = False
            adj[a][b] = True
            indeg[a] -= 1
            indeg[b] += 1
    
    # 3. 위상정렬
    q = deque()
    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)
    
    result = []
    certain = True
    
    for _ in range(n):
        if not q:                # indegree 0이 하나도 없다 → 사이클
            certain = False
            result = "IMPOSSIBLE"
            break
        if len(q) > 1:          # indegree 0이 여러 개 → 순위 불확실
            certain = False
        
        now = q.popleft()
        result.append(now)
        
        for nxt in range(1, n+1):
            if adj[now][nxt]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)
    
    if result == "IMPOSSIBLE":
        print("IMPOSSIBLE")
    else:
        if not certain:
            print("?")
        else:
            print(*result)
