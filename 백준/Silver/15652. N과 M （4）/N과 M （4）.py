import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = []
out = []

def dfs(start: int, depth: int):
    if depth == M:
        out.append(' '.join(map(int.__str__, seq)))
        return
    for x in range(start, N + 1):
        seq.append(x)
        dfs(x, depth + 1)   # x 이상만 허용 → 비내림차순 보장
        seq.pop()

dfs(1, 0)
sys.stdout.write('\n'.join(out))
