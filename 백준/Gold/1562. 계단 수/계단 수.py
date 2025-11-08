MOD = 1_000_000_000

N = int(input())

# dp[length][last_digit][mask]
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]

# 초기 상태: 첫 자리 1~9
for d in range(1, 10):
    dp[1][d][1 << d] = 1

for length in range(2, N + 1):
    for last in range(10):
        for mask in range(1 << 10):
            if dp[length - 1][last][mask] == 0:
                continue
            cur = dp[length - 1][last][mask]

            # 다음 자리 후보
            for nxt in (last - 1, last + 1):
                if 0 <= nxt <= 9:
                    dp[length][nxt][mask | (1 << nxt)] = (dp[length][nxt][mask | (1 << nxt)] + cur) % MOD

# 모든 숫자(0~9) 사용한 상태: mask == (1<<10)-1 == 1023
FULL = (1 << 10) - 1

answer = 0
for d in range(10):
    answer = (answer + dp[N][d][FULL]) % MOD

print(answer)
