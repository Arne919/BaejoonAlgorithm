text = input().rstrip()
bomb = input().rstrip()
stack = []
bomb_len = len(bomb)

for ch in text:
    stack.append(ch)
    # 폭발 문자열과 끝부분이 일치하면 제거
    if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]

# 결과 출력
result = ''.join(stack)
print(result if result else "FRULA")
