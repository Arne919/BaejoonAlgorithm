A = input().strip()
B = input().strip()
C = input().strip()

# 숫자로 계산
num_result = int(A) + int(B) - int(C)

# 문자열로 계산
str_concat = A + B
str_result = int(str_concat) - int(C)

print(num_result)
print(str_result)
