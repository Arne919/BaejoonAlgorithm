import sys
import bisect

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = []

for x in arr:
    pos = bisect.bisect_left(dp, x)
    if pos == len(dp):
        dp.append(x)
    else:
        dp[pos] = x

print(len(dp))
