# Python 3
import sys
from functools import cmp_to_key

input = sys.stdin.readline

def cmp(a, b):
    # a, b 는 (index, T, S)
    _, Ta, Sa = a
    _, Tb, Sb = b
    # compare Sa/Ta and Sb/Tb by cross-multiplication
    left = Sa * Tb
    right = Sb * Ta
    if left > right:
        return -1  # a 먼저
    if left < right:
        return 1   # b 먼저
    # 비율 같으면 인덱스 작은 것 먼저
    return a[0] - b[0]

def main():
    n = int(input().strip())
    jobs = []
    for i in range(1, n+1):
        line = input().split()
        if not line:
            line = input().split()
        t = int(line[0]); s = int(line[1])
        jobs.append((i, t, s))
    jobs.sort(key=cmp_to_key(cmp))
    print(" ".join(str(job[0]) for job in jobs))

if __name__ == "__main__":
    main()
