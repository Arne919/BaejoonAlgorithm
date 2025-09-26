import sys
input = sys.stdin.readline

# 세그먼트 트리 초기화
def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

# 구간 합
def query(node, start, end, left, right):
    if right < start or end < left:  # 겹치지 않는 구간
        return 0
    if left <= start and end <= right:  # 완전히 포함되는 구간
        return tree[node]
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

# 특정 원소 변경
def update(node, start, end, idx, diff):
    if idx < start or idx > end:  # 범위 밖
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, idx, diff)
        update(node*2+1, mid+1, end, idx, diff)

# 입력
N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

tree = [0] * (4 * N)  # 세그먼트 트리 배열
init(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:  # b번째 수를 c로 변경
        b -= 1  # 인덱스 보정
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, N-1, b, diff)
    else:  # 구간 합
        print(query(1, 0, N-1, b-1, c-1))
