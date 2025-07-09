word = input().upper()
alphabet_count = [0] * 26

for char in word:
    alphabet_count[ord(char) - ord('A')] += 1

max_count = max(alphabet_count)
if alphabet_count.count(max_count) > 1:
    print('?')
else:
    print(chr(alphabet_count.index(max_count) + ord('A')))
