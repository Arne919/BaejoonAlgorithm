import sys

n = int(sys.stdin.readline())
points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.sort(key=lambda p: (p[1], p[0]))

for x, y in points:
    print(x, y)
