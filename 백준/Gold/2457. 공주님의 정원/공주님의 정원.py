import sys
input = sys.stdin.readline

def to_md(m, d):
    return m*100 + d

N = int(input())
flowers = []
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    s = to_md(sm, sd)
    e = to_md(em, ed)
    flowers.append((s, e))

# 시작일 오름차순, 시작일 같으면 지는 날 내림차순
flowers.sort(key=lambda x: (x[0], -x[1]))

TARGET_START = 301   # 3/1
TARGET_END   = 1201  # 12/1

cnt = 0
idx = 0
cur = TARGET_START

while cur < TARGET_END:
    best_end = cur
    while idx < N and flowers[idx][0] <= cur:
        if flowers[idx][1] > best_end:
            best_end = flowers[idx][1]
        idx += 1

    if best_end == cur:
        print(0)
        break

    cnt += 1
    cur = best_end

else:
    print(cnt)
