X = int(input())

# 대각선 번호 찾기
n = 1
while X > n * (n + 1) // 2:
    n += 1

# n번째 대각선에서의 위치
pos = X - (n - 1) * n // 2

if n % 2 == 0:  # 짝수 대각선
    num = pos
    den = n - pos + 1
else:  # 홀수 대각선
    num = n - pos + 1
    den = pos

print(f"{num}/{den}")
