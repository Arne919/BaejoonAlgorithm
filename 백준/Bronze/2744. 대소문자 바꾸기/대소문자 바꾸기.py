s = input()
result = ""

for ch in s:
    if 'a' <= ch <= 'z':     # 소문자면
        result += chr(ord(ch) - 32)
    else:                   # 대문자면
        result += chr(ord(ch) + 32)

print(result)
