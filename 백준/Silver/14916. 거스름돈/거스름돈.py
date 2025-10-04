n = int(input().strip())

answer = -1
for five in range(n // 5, -1, -1):  # 5원 개수를 최대치부터 줄여가며
    rest = n - five * 5
    if rest % 2 == 0:
        two = rest // 2
        answer = five + two
        break

print(answer)
