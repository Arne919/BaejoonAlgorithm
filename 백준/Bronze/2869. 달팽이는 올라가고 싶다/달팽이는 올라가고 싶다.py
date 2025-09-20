A, B, V = map(int, input().split())

# (V - A)를 하루 실질 진행량 (A - B)로 나눔
days = (V - A) // (A - B) + 1
if (V - A) % (A - B) != 0:
    days += 1

print(days)
