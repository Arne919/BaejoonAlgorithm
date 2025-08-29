import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축(halving)
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    # 랭크/사이즈 없어도 N이 작아서 충분히 빠르지만, 작은 루트를 큰 루트에 붙이기
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

N = int(input())
M = int(input())

adj = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

# DSU 초기화 (1-indexed 처리 위해 N+1)
parent = [i for i in range(N+1)]
size = [1]*(N+1)

# 인접행렬 기반 union
for i in range(N):
    row = adj[i]
    for j in range(N):
        if row[j] == 1:
            union(i+1, j+1)

# 여행 계획의 모든 도시가 같은 컴포넌트인지 확인
root0 = find(plan[0])
ok = all(find(city) == root0 for city in plan)

print("YES" if ok else "NO")
