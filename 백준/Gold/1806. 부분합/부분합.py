import sys

input = sys.stdin.readline
N, S = map(int, input().split())
arr = list(map(int, input().split()))

INF = 10**9
ans = INF
left = 0
curr = 0

for right in range(N):
    curr += arr[right]
    # 합이 S 이상이 되는 동안 왼쪽을 줄여 최소 길이 갱신
    while curr >= S:
        ans = min(ans, right - left + 1)
        curr -= arr[left]
        left += 1

print(0 if ans == INF else ans)
