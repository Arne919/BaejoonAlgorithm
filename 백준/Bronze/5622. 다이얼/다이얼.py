s = input().strip()
groups = [
    ("ABC", 3),
    ("DEF", 4),
    ("GHI", 5),
    ("JKL", 6),
    ("MNO", 7),
    ("PQRS", 8),
    ("TUV", 9),
    ("WXYZ", 10),
]

time = 0
for ch in s:
    for letters, t in groups:
        if ch in letters:
            time += t
            break

print(time)
