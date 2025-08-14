import sys
input = sys.stdin.readline

T = int(input())
max_n = 40

# DP 배열 준비
count0 = [0] * (max_n + 1)
count1 = [0] * (max_n + 1)

# 초기값
count0[0], count1[0] = 1, 0
count0[1], count1[1] = 0, 1

# 점화식으로 채우기
for i in range(2, max_n + 1):
    count0[i] = count0[i-1] + count0[i-2]
    count1[i] = count1[i-1] + count1[i-2]

# 테스트 케이스 처리
for _ in range(T):
    n = int(input())
    print(count0[n], count1[n])
