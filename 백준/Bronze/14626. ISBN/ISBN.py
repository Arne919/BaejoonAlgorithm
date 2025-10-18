isbn = input().strip()

# 가중치 패턴: 1, 3, 1, 3, ..., 총 13자리
weights = [1 if i % 2 == 0 else 3 for i in range(13)]

# 손상된 자리의 인덱스와 나머지 합 계산
missing_idx = isbn.index('*')
total = 0

for i in range(13):
    if i == missing_idx:
        continue
    total += int(isbn[i]) * weights[i]

# 0~9 중 어떤 숫자를 넣었을 때 10의 배수가 되는지 확인
for x in range(10):
    if (total + x * weights[missing_idx]) % 10 == 0:
        print(x)
        break
