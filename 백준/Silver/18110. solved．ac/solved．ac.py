import sys

input = sys.stdin.readline

n = int(input().strip())

if n == 0:
    print(0)
else:
    opinions = [int(input().strip()) for _ in range(n)]
    opinions.sort()
    
    cut = int(n * 0.15 + 0.5)  # 15% 반올림
    trimmed = opinions[cut:n - cut]
    avg = sum(trimmed) / len(trimmed)
    
    print(int(avg + 0.5))  # 최종 평균도 반올림
