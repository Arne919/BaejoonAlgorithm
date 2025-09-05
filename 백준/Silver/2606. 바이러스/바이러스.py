import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n = int(input().strip())          # 컴퓨터 수 (1..n)
    m = int(input().strip())          # 간선 수

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * (n + 1)
    q = deque([1])
    visited[1] = True
    infected = 0

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                infected += 1      # 1을 통해 새로 감염되는 컴퓨터
                q.append(nxt)

    print(infected)

if __name__ == "__main__":
    solve()
