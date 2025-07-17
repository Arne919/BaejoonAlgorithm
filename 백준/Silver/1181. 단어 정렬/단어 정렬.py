n = int(input())
words = set(input().strip() for _ in range(n))

sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)
