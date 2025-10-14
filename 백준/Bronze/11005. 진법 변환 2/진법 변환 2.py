N, B = input().split()
N = int(N)
B = int(B)

digits = []
while N > 0:
    r = N % B
    if r < 10:
        digits.append(str(r))
    else:
        digits.append(chr(r + 55))  # 10 → A (65-10)
    N //= B

print(''.join(reversed(digits)))
