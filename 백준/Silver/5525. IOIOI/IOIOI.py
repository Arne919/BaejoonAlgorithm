import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().strip()

answer = 0      # 최종 정답
cnt = 0         # IOI 연속 등장 횟수
i = 0

while i < M - 2:
    if S[i:i+3] == 'IOI':
        cnt += 1
        if cnt >= N:
            answer += 1
        i += 2
    else:
        cnt = 0
        i += 1

print(answer)
