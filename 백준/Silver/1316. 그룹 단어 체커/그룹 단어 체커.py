n = int(input())
count = 0

for _ in range(n):
    word = input()
    seen = set()
    is_group = True
    prev = ""

    for ch in word:
        if ch != prev:
            if ch in seen:
                is_group = False
                break
            seen.add(ch)
        prev = ch

    if is_group:
        count += 1

print(count)
