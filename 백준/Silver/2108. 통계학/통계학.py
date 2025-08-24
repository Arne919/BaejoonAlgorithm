import sys
input = sys.stdin.readline

N = int(input())
OFFSET = 4000
cnt = [0] * (8001)

s = 0
min_v, max_v = 4001, -4001

for _ in range(N):
    x = int(input())
    s += x
    cnt[x + OFFSET] += 1
    if x < min_v: min_v = x
    if x > max_v: max_v = x

# 1) 산술평균 (소수 첫째 자리 반올림, half-up)
avg = s / N
if avg >= 0:
    mean = int(avg + 0.5)
else:
    mean = int(avg - 0.5)

# 2) 중앙값
target = (N + 1) // 2
acc = 0
median = 0
for i in range(8001):
    acc += cnt[i]
    if acc >= target:
        median = i - OFFSET
        break

# 3) 최빈값 (여러 개면 두 번째로 작은 값)
max_c = max(cnt)
modes = [i - OFFSET for i, c in enumerate(cnt) if c == max_c]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]

# 4) 범위
rng = max_v - min_v

print(mean)
print(median)
print(mode)
print(rng)
