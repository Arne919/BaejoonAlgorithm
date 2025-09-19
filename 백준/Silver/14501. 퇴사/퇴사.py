N = int(input())
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
    
dp = [0] * (N+2)  # N+1까지 필요

for i in range(N, 0, -1):  # N일부터 1일까지 거꾸로
    if i + T[i-1] - 1 <= N:  # 상담이 가능한 경우
        dp[i] = max(P[i-1] + dp[i + T[i-1]], dp[i+1])
    else:  # 상담 불가능 → 그냥 넘어감
        dp[i] = dp[i+1]
        
print(dp[1])