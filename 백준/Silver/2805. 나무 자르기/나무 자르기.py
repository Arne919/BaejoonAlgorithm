import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
trees = list(map(int, input().split()))

# 이진 탐색
left = 0
right = max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2

    # 조건을 만족하는 나무만 대상으로 잘린 길이 계산
    total = sum(tree - mid for tree in trees if tree > mid)

    if total >= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
