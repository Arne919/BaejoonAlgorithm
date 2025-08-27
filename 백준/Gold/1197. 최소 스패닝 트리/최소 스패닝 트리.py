import sys
input = sys.stdin.readline

# 유니온-파인드 (경로 압축 + 랭크/사이즈)
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path halving
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 가중치 기준 정렬 (음수 포함 OK)
edges.sort()

parent = list(range(V + 1))
size = [1] * (V + 1)

mst_weight = 0
picked = 0

for w, u, v in edges:
    if union(u, v):
        mst_weight += w
        picked += 1
        if picked == V - 1:
            break

print(mst_weight)
