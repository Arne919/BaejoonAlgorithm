import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

# 인접 리스트
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))  # 무방향

def dfs(start):
    visited = [False] * (n + 1)
    max_dist = 0
    far_node = start

    def go(node, dist):
        nonlocal max_dist, far_node
        visited[node] = True

        if dist > max_dist:
            max_dist = dist
            far_node = node

        for next_node, w in tree[node]:
            if not visited[next_node]:
                go(next_node, dist + w)

    go(start, 0)
    return far_node, max_dist

node, _ = dfs(1)

_, diameter = dfs(node)

print(diameter)
