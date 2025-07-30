import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

prefix = 0
mod_count = [0] * M
mod_count[0] = 1  # 처음에 누적합이 0이면 바로 한 구간
answer = 0

for num in A:
    prefix = (prefix + num) % M
    answer += mod_count[prefix]
    mod_count[prefix] += 1

print(answer)
