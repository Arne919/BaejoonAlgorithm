import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n = next(it); m = next(it)

    parent = list(range(n))
    size = [1]*n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path halving
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False  # 이미 같은 집합 -> 이 간선이 사이클을 만든다
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    # 간선들을 차례대로 처리
    for i in range(1, m+1):
        a = next(it); b = next(it)
        if not union(a, b):
            print(i)
            return
    print(0)

if __name__ == "__main__":
    solve()
