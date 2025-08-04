N = int(input())
P = list(map(int, input().split()))

P.sort()  # 시간 적은 순서로 정렬

total = 0  # 전체 최소 시간 합
acc = 0    # 누적 시간

for p in P:
    acc += p      # 지금 사람까지 걸리는 시간
    total += acc  # 전체 누적 시간에 더함

print(total)
