n = int(input())
A = list(map(int, input().split()))

dp = A[:]  # 자기 자신만 있는 수열의 합으로 초기화

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))
