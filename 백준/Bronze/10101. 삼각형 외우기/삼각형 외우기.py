# 세 각 입력 받기
a = int(input())
b = int(input())
c = int(input())

# 각의 합 계산
total = a + b + c

# 조건 분기
if a == b == c == 60:
    print("Equilateral")
elif total == 180 and (a == b or b == c or a == c):
    print("Isosceles")
elif total == 180 and (a != b and b != c and a != c):
    print("Scalene")
else:
    print("Error")
