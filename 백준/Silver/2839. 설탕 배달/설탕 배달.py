N = int(input())

for five in range(N // 5, -1, -1):  # 5kg 최대 개수부터 줄여감
    remain = N - 5 * five
    if remain % 3 == 0:
        three = remain // 3
        print(five + three)
        break
else:
    print(-1)
