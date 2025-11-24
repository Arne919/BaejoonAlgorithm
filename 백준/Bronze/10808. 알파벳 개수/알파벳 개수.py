S = input().strip()

count = [0] * 26  # a~z 카운트 리스트

for ch in S:
    count[ord(ch) - ord('a')] += 1

print(*count)
