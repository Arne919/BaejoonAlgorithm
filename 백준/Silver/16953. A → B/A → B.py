A, B = map(int, input().split())

count = 1  # 연산 횟수 + 1 형태로 셀 것

while B != A:
    count += 1
    if B < A:
        print(-1)
        exit()
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        print(-1)
        exit()

print(count)
