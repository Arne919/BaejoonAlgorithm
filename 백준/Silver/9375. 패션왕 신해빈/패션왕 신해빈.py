import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}

    for _ in range(n):
        name, kind = input().split()
        if kind not in clothes:
            clothes[kind] = 0
        clothes[kind] += 1

    result = 1
    for kind in clothes:
        result *= (clothes[kind] + 1)
    print(result - 1)
