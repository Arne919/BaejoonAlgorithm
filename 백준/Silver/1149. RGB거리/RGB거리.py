import sys

input = sys.stdin.readline

N = int(input().strip())
r, g, b = map(int, input().split())
# dpR, dpG, dpB: i번째 집까지 칠했을 때 마지막 색을 R/G/B로 한 최소비용
dpR, dpG, dpB = r, g, b

for _ in range(1, N):
    r, g, b = map(int, input().split())
    newR = r + min(dpG, dpB)
    newG = g + min(dpR, dpB)
    newB = b + min(dpR, dpG)
    dpR, dpG, dpB = newR, newG, newB

print(min(dpR, dpG, dpB))
