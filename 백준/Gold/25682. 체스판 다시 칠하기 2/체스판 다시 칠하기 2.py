import sys

# 입력: 체스판 크기 N x M, 검사할 부분 크기 K x K
N, M, K = map(int, sys.stdin.readline().split())

# 체스판 입력 받기 (N줄)
board = list(list(sys.stdin.readline().rstrip()) for _ in range(N))

# 시작 색깔(start_color)이 'B' 또는 'W'일 때,
# 전체 체스판에서 K x K 크기의 부분 체스판을 골라
# 색을 칠하는 데 드는 최소 비용(바꿔야 하는 칸 수)을 반환하는 함수
def check(start_color):
    # 누적합(Prefix Sum) 배열 초기화
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    # 체스판 각 칸을 기준으로, 잘못된 색깔의 칸은 1, 맞는 칸은 0으로 누적합 계산
    for row in range(N):
        for col in range(M):
            # (row+col)의 짝/홀 여부로 색이 번갈아야 하는 위치를 판단
            if ((row + col) % 2 == 0):
                # 현재 칸이 시작 색과 다르면 수정이 필요함 (1)
                v = (board[row][col] != start_color)
            else:
                # 현재 칸이 시작 색과 같으면 수정이 필요함 (1)
                v = (board[row][col] == start_color)

            # 2차원 누적합 구하기
            dp[row + 1][col + 1] = (
                dp[row][col + 1] + 
                dp[row + 1][col] - 
                dp[row][col] + 
                v
            )

    # 최소 변경 횟수를 큰 값으로 초기화
    MIN = N * M

    # 모든 K x K 부분 체스판에 대해 누적합을 이용해 변경 횟수 계산
    for row in range(1, N - K + 2):
        for col in range(1, M - K + 2):
            # 부분합 계산 (누적합 테크닉)
            total = (
                dp[row + K - 1][col + K - 1] - 
                dp[row + K - 1][col - 1] - 
                dp[row - 1][col + K - 1] + 
                dp[row - 1][col - 1]
            )
            # 최소값 갱신
            MIN = min(MIN, total)

    return MIN

# 'B'로 시작하거나 'W'로 시작할 때 각각 최소 변경 횟수를 구해 비교
answer = min(check('B'), check('W'))

# 결과 출력
print(answer)
