def d(n):
    return n + sum(map(int, str(n)))

generated = [False] * 10001

for i in range(1, 10001):
    dn = d(i)
    if dn <= 10000:
        generated[dn] = True

for i in range(1, 10001):
    if not generated[i]:
        print(i)
