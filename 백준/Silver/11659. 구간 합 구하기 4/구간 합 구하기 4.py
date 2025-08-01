import sys
input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합 배열 생성
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])
