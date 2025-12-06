def recursion(s, l, r, cnt):
    cnt[0] += 1  # 호출 횟수 증가
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    cnt = [0]      # 리스트로 넘겨야 참조 가능
    result = recursion(s, 0, len(s)-1, cnt)
    return result, cnt[0]

T = int(input())
for _ in range(T):
    S = input().strip()
    res, c = isPalindrome(S)
    print(res, c)
