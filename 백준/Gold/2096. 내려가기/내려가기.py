import sys
input = sys.stdin.readline

N = int(input())
a, b, c = map(int, input().split())

maxDP = [a, b, c]
minDP = [a, b, c]

for _ in range(N - 1):
    a, b, c = map(int, input().split())

    # 이전 DP 값을 복사해둠
    prev_max = maxDP[:]
    prev_min = minDP[:]

    # 최대 DP 갱신
    maxDP[0] = a + max(prev_max[0], prev_max[1])
    maxDP[1] = b + max(prev_max[0], prev_max[1], prev_max[2])
    maxDP[2] = c + max(prev_max[1], prev_max[2])

    # 최소 DP 갱신
    minDP[0] = a + min(prev_min[0], prev_min[1])
    minDP[1] = b + min(prev_min[0], prev_min[1], prev_min[2])
    minDP[2] = c + min(prev_min[1], prev_min[2])

print(max(maxDP), min(minDP))
