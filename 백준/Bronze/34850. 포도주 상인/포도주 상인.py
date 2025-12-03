import sys
input = sys.stdin.readline

x, y, p, a, b = map(int, input().split())

# 계산 (파이썬은 큰 정수 자동 처리)
ans = p * x + b * x * (y - 1) - a * x * (x - 1) // 2
print(ans)
