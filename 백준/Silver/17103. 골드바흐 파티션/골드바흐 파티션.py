import sys
input = sys.stdin.readline

# 소수 판별 테이블 생성
MAX = 1_000_000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

# 입력 처리
T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    for i in range(2, N // 2 + 1):
        if is_prime[i] and is_prime[N - i]:
            count += 1
    print(count)
