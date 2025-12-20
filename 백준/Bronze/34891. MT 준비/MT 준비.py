N, M = map(int, input().split())

if N == 0:
    print(0)
else:
    print((N + M - 1) // M)
