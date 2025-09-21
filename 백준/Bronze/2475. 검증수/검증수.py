# 입력 받기
numbers = list(map(int, input().split()))

# 각 숫자를 제곱한 뒤 합산
total = sum(n ** 2 for n in numbers)

# 10으로 나눈 나머지
result = total % 10

print(result)
