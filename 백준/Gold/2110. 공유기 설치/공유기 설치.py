import sys
input = sys.stdin.readline

# 입력
n, c = map(int, input().split())
houses = sorted(int(input()) for _ in range(n))

# 이분 탐색
start = 1
end = houses[-1] - houses[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    last_position = houses[0]

    for i in range(1, n):
        if houses[i] - last_position >= mid:
            count += 1
            last_position = houses[i]

    if count >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
