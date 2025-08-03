import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

left = 1
right = max(lines)
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(line // mid for line in lines)

    if count >= N:
        answer = mid  # 최대 길이 갱신
        left = mid + 1
    else:
        right = mid - 1

print(answer)
