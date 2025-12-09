import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))

arr.sort()
left, right = 0, N - 1
count = 0

while left < right:
    s = arr[left] + arr[right]
    
    if s == M:
        count += 1
        left += 1
        right -= 1
    elif s < M:
        left += 1
    else:
        right -= 1

print(count)
