import sys
input = sys.stdin.readline

N = int(input())

# 2부터 sqrt(N)까지 검사
i = 2
while i * i <= N:
    while N % i == 0:
        print(i)
        N //= i
    i += 1

# 마지막에 N이 1이 아니면 소수이므로 출력
if N > 1:
    print(N)
