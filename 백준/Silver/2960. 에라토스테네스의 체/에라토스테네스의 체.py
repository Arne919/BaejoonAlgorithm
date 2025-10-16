N, K = map(int, input().split())

erased_count = 0
is_erased = [False] * (N + 1)  # 0~N까지

for i in range(2, N + 1):
    if not is_erased[i]:  # 아직 안 지워졌다면
        for j in range(i, N + 1, i):
            if not is_erased[j]:  # 아직 안 지워졌으면
                is_erased[j] = True
                erased_count += 1
                if erased_count == K:
                    print(j)
                    exit()  # 프로그램 종료
