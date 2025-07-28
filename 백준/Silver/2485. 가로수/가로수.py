import sys
import math

input = sys.stdin.readline

# 입력
N = int(input())
trees = [int(input()) for _ in range(N)]

# 인접한 가로수 간격 구하기
diffs = [trees[i+1] - trees[i] for i in range(N-1)]

# 모든 간격의 최대공약수 구하기
g = diffs[0]
for d in diffs[1:]:
    g = math.gcd(g, d)

# 전체 구간 길이
total_length = trees[-1] - trees[0]

# 전체 필요한 나무 수
needed = total_length // g + 1

# 새로 심어야 할 나무 수
print(needed - N)
