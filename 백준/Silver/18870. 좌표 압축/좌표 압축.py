import sys

input = sys.stdin.readline

n = int(input())
coords = list(map(int, input().split()))

sorted_unique = sorted(set(coords))

rank = {value: idx for idx, value in enumerate(sorted_unique)}

result = [str(rank[x]) for x in coords]
print(' '.join(result))
