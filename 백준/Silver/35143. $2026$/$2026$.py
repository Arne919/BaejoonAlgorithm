N = int(input())

# 고려대학교 개교 원년
FOUNDATION = 1905

if N == 1:
    X = 1
else:
    k = (N - 3) // 2
    root = "1" + "0" * k + "1"
    X = int(root) ** 2

print(FOUNDATION + X)
