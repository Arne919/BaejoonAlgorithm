import sys
input = sys.stdin.readline

# 세그먼트 트리 함수
def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build(node * 2, start, mid)
        build(node * 2 + 1, mid + 1, end)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def query(node, start, end, left, right):
    if right < start or end < left:
        return float('inf')  # 범위를 벗어나면 무한대 반환
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    l_min = query(node * 2, start, mid, left, right)
    r_min = query(node * 2 + 1, mid + 1, end, left, right)
    return min(l_min, r_min)

# 입력 처리
N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)

# 세그먼트 트리 구성
build(1, 0, N - 1)

# 쿼리 처리
for _ in range(M):
    a, b = map(int, input().split())
    print(query(1, 0, N - 1, a - 1, b - 1))
