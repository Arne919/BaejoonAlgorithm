import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pw = {}

for _ in range(N):
    site, password = input().split()
    pw[site] = password

for _ in range(M):
    site = input().strip()
    print(pw[site])
