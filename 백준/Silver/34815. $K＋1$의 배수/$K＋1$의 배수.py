import sys

N, K = map(int, sys.stdin.readline().split())
if K % 2 == 0 or N >= K + 1:
    print("YES")
else:
    print("NO")
