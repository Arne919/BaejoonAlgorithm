def z_visit(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    area = half * half

    # 좌상단
    if r < half and c < half:
        return z_visit(n - 1, r, c)
    # 우상단
    elif r < half and c >= half:
        return area + z_visit(n - 1, r, c - half)
    # 좌하단
    elif r >= half and c < half:
        return 2 * area + z_visit(n - 1, r - half, c)
    # 우하단
    else:
        return 3 * area + z_visit(n - 1, r - half, c - half)


# 입력
N, r, c = map(int, input().split())
print(z_visit(N, r, c))
