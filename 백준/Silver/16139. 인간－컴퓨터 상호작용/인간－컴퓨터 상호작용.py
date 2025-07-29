import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())

# count[i] = S[0:i]까지 각 알파벳 누적 개수를 담은 리스트
count = {0: [0] * 26}

for i, ch in enumerate(S):
    count[i + 1] = count[i][:]  # 리스트 복사
    count[i + 1][ord(ch) - ord('a')] += 1

for _ in range(q):
    ch, l, r = input().split()
    l = int(l)
    r = int(r)
    idx = ord(ch) - ord('a')
    print(count[r + 1][idx] - count[l][idx])
