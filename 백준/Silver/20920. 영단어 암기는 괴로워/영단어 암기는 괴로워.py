import sys
input = sys.stdin.readline

N, M = map(int, input().split())
freq = {}

for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    freq[word] = freq.get(word, 0) + 1

# 정렬 기준:
# 1. 빈도 내림차순
# 2. 길이 내림차순
# 3. 사전순 오름차순
words = sorted(freq.keys(), key=lambda w: (-freq[w], -len(w), w))

for w in words:
    print(w)
