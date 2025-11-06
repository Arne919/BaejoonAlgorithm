# Python 3
import sys
import math
from itertools import permutations

pts = [tuple(map(int, sys.stdin.readline().split())) for _ in range(4)]
start = pts[0]
others = pts[1:]

def dist(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

min_total = float('inf')
for order in permutations(others):
    total = 0.0
    cur = start
    for p in order:
        total += dist(cur, p)
        cur = p
    if total < min_total:
        min_total = total

# 소수점 이하 버리기 (양수이므로 int()가 floor와 동일)
print(int(min_total))
