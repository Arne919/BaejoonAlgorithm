import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0

for ai in A:
    # 총감독관 1명
    result += 1

    remain = ai - B
    if remain > 0:
        # 부감독관 수 계산 (올림 나눗셈)
        result += (remain + C - 1) // C

print(result)
