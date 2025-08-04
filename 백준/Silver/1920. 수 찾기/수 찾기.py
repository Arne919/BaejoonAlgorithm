import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

for x in targets:
    print(1 if x in A else 0)
