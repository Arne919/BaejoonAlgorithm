def intersect(a, b):
    l = max(a[0], b[0])
    r = min(a[1], b[1])
    if l > r:
        return None
    return (l, r)

N = int(input())
LR = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10**18

safe = (-INF, INF)   # 실패 0회
used = None          # 실패 1회

for i in range(N):
    L, R = LR[i]

    safe_next = None
    used_next = None

    # 1️⃣ safe 상태 이동 + 교집합
    if safe is not None:
        moved_safe = (safe[0] - 1, safe[1] + 1)
        safe_next = intersect(moved_safe, (L, R))

    # 2️⃣ used 상태 이동 + 교집합
    used_candidates = []

    if used is not None:
        moved_used = (used[0] - 1, used[1] + 1)
        t = intersect(moved_used, (L, R))
        if t:
            used_candidates.append(t)

    # 3️⃣ 이번 초에 실패를 사용하는 경우 (safe → used)
    if safe is not None:
        moved_safe = (safe[0] - 1, safe[1] + 1)
        used_candidates.append(moved_safe)

    # used 후보 합치기
    for c in used_candidates:
        if used_next is None:
            used_next = c
        else:
            used_next = (min(used_next[0], c[0]), max(used_next[1], c[1]))

    safe = safe_next
    used = used_next

    if safe is None and used is None:
        print("Surrender")
        exit()

print("World Champion")
