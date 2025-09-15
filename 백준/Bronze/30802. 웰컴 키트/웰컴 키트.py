import sys
import math

data = sys.stdin.read().strip().split()
N = int(data[0])
counts = list(map(int, data[1:7]))  # S, M, L, XL, XXL, XXXL
T = int(data[7])
P = int(data[8])

# 티셔츠: 각 사이즈별 ceil(count/T) 합
tshirt_bundles = sum((c + T - 1) // T for c in counts)

# 펜: P자루 묶음 최대, 나머지를 1자루씩
pen_bundles = N // P
single_pens = N - pen_bundles * P

print(tshirt_bundles)
print(pen_bundles, single_pens)
