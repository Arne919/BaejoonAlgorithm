import sys

N, M, A, B = map(int, sys.stdin.readline().split())
need = max(0, 3 * N - M)
print(0 if need == 0 else B + A * need)
