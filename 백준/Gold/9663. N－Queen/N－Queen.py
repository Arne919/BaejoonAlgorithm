import sys
input = sys.stdin.readline

N = int(input())
count = 0

col = [False] * N
diag1 = [False] * (2 * N)   # ↘ 대각선 (row+col)
diag2 = [False] * (2 * N)   # ↙ 대각선 (row-col+N-1)

def dfs(row):
    global count
    if row == N:   # 모든 행에 퀸을 다 놓음
        count += 1
        return
    
    for c in range(N):
        if not col[c] and not diag1[row+c] and not diag2[row-c+N-1]:
            col[c] = diag1[row+c] = diag2[row-c+N-1] = True
            dfs(row+1)
            col[c] = diag1[row+c] = diag2[row-c+N-1] = False  # 백트래킹

dfs(0)
print(count)
