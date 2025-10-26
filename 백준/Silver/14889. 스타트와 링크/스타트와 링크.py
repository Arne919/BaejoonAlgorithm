import sys
from itertools import combinations

input = sys.stdin.readline

def main():
    N = int(input().strip())
    S = [list(map(int, input().split())) for _ in range(N)]
    # pair_sum[i][j] = S[i][j] + S[j][i]  (i < j 만 사용할 것)
    pair_sum = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            pair_sum[i][j] = S[i][j] + S[j][i]

    min_diff = float('inf')
    players = list(range(1, N))  # 0번은 항상 스타트 팀에 고정

    # 0번을 포함한 스타트 팀을 선택 (나머지 N/2-1명을 players에서 선택)
    for comb in combinations(players, N//2 - 1):
        start_team = (0,) + comb
        link_team = [i for i in range(N) if i not in start_team]

        # 스타트 팀 능력치
        start_sum = 0
        for i_idx in range(len(start_team)):
            for j_idx in range(i_idx+1, len(start_team)):
                i = start_team[i_idx]; j = start_team[j_idx]
                a, b = (i, j) if i < j else (j, i)
                start_sum += pair_sum[a][b]

        # 링크 팀 능력치
        link_sum = 0
        for i_idx in range(len(link_team)):
            for j_idx in range(i_idx+1, len(link_team)):
                i = link_team[i_idx]; j = link_team[j_idx]
                a, b = (i, j) if i < j else (j, i)
                link_sum += pair_sum[a][b]

        diff = abs(start_sum - link_sum)
        if diff < min_diff:
            min_diff = diff
            if min_diff == 0:
                break  # 더 이상 작아질 수 없음

    print(min_diff)

if __name__ == "__main__":
    main()
