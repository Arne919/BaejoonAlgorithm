import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    empty = 0
    for _ in range(N):
        row = input().strip()
        empty += row.count('.')
    
    if empty % 2 == 1:
        print("sewon")
    else:
        print("pizza")
