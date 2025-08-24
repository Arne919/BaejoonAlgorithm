import sys
input = sys.stdin.readline

MOD = 998244353

N = int(input().strip())
A = list(map(int, input().split()))

cntSame = sum(1 for i, a in enumerate(A, 1) if a == i)

ans = pow(N - 1, cntSame, MOD) * pow(N - 2, N - cntSame, MOD) % MOD
print(ans)
