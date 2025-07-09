# A와 B를 입력받아 정수로 변환
A, B = map(int, input().split())

# 조건에 따라 출력
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
