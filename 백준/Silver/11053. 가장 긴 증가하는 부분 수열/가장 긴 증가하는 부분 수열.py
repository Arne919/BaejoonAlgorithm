import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

tails = []  # 길이 k인 증가 부분수열들의 "마지막 값"의 최소들을 저장
for x in A:
    i = bisect_left(tails, x)  # strict 증가 → 첫 >= x 위치
    if i == len(tails):
        tails.append(x)
    else:
        tails[i] = x

print(len(tails))
