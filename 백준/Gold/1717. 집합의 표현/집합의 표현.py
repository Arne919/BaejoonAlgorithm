import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path halving
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

out_lines = []
for _ in range(m):
    t, a, b = map(int, input().split())
    if t == 0:
        union(a, b)
    else:  # t == 1
        out_lines.append("YES" if find(a) == find(b) else "NO")

print("\n".join(out_lines))
