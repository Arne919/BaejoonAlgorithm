import sys
input = sys.stdin.readline

N, M = map(int, input().split())

used = [False] * (N + 1)
path = []
out = []

def dfs():
    if len(path) == M:
        out.append(' '.join(map(str, path)))
        return
    for x in range(1, N + 1):
        if not used[x]:
            used[x] = True
            path.append(x)
            dfs()
            path.pop()
            used[x] = False

dfs()
sys.stdout.write('\n'.join(out))
