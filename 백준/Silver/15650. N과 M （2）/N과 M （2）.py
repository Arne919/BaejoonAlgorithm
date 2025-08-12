import sys
input = sys.stdin.readline

N, M = map(int, input().split())
out = []

def dfs(start, comb):
    if len(comb) == M:
        out.append(' '.join(map(str, comb)))
        return
    for x in range(start, N + 1):
        comb.append(x)
        dfs(x + 1, comb)
        comb.pop()

dfs(1, [])
sys.stdout.write('\n'.join(out))
