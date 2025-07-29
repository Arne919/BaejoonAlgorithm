import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())

prefix = [[0] * (len(S) + 1) for _ in range(26)]

for i in range(len(S)):
    c = ord(S[i]) - ord('a')
    for j in range(26):
        prefix[j][i+1] = prefix[j][i] + (1 if j == c else 0)

for _ in range(q):
    ch, l, r = input().split()
    l = int(l)
    r = int(r)
    c = ord(ch) - ord('a')
    print(prefix[c][r+1] - prefix[c][l])
