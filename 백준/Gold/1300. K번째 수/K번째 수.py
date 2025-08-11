import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

left, right = 1, N * N
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = 0
   
    for i in range(1, N + 1):
        count += min(N, mid // i)
    
    if count >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
