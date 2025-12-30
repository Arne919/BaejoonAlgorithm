import sys
input = sys.stdin.readline

N = int(input())

# 초기값을 충분히 큰 값 / 작은 값으로 설정
min_x = 100000
max_x = -100000
min_y = 100000
max_y = -100000

for _ in range(N):
    x, y = map(int, input().split())
    
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

# 최소 외접 직사각형의 넓이
area = (max_x - min_x) * (max_y - min_y)
print(area)
