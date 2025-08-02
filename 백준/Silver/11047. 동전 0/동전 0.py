import sys

input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# 큰동전부터 사용하기위해 내림차순 정렬
coins.sort(reverse=True)

count = 0
for coin in coins:
    if K == 0:
        break
    count += K // coin  # 해당동전으로 만들수있는 최대개수
    K %= coin           # 남은금액

print(count)
