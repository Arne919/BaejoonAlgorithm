N, M = map(int, input().split())

# 초기 바구니 상태
basket = [i for i in range(1, N+1)]

# M번 교환 처리
for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

# 결과 출력
print(*basket)
