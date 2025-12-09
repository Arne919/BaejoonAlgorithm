import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

lenA = len(A)
lenB = len(B)

# DP 테이블 (LCS 길이 저장)
dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]

# DP 채우기
for i in range(1, lenA + 1):
    for j in range(1, lenB + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS 길이 출력
print(dp[lenA][lenB])

# LCS 문자열 복원
i, j = lenA, lenB
lcs = []

while i > 0 and j > 0:
    if A[i - 1] == B[j - 1]:  # 같은 문자면 LCS에 포함
        lcs.append(A[i - 1])
        i -= 1
        j -= 1
    else:
        # 더 큰 값으로 이동
        if dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

# LCS가 존재하면 출력 (역순이므로 뒤집기)
if dp[lenA][lenB] > 0:
    print(''.join(reversed(lcs)))
