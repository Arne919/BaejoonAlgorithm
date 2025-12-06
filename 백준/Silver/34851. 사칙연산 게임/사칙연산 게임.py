import sys
input = sys.stdin.readline

MOD = 10**9 + 7

N = int(input())
a = list(map(int, input().split()))

val = a[0] % MOD
is_one = (a[0] == 1)

for x in a[1:]:
    if is_one or x == 1:
        # 덧셈
        val = (val + x) % MOD
        is_one = False  # 합은 1이 될 수 없음
    else:
        # 곱셈
        val = (val * (x % MOD)) % MOD
        # 곱셈 후 결과가 1이 되는 경우 없음 (둘 다 >1이므로)
        is_one = False

print(val)
