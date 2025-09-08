import sys

input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))
x = int(input().strip())

arr.sort()
left, right = 0, n - 1
cnt = 0

while left < right:
    s = arr[left] + arr[right]
    if s == x:
        cnt += 1
        left += 1
        right -= 1
    elif s < x:
        left += 1
    else:
        right -= 1

print(cnt)
