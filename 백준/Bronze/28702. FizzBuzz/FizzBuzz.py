def fb(x: int) -> str:
    if x % 15 == 0:
        return "FizzBuzz"
    if x % 3 == 0:
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"
    return str(x)

def residues_for(token: str):
    if token == "FizzBuzz":
        return {0}
    if token == "Fizz":
        return {3,6,9,12}
    if token == "Buzz":
        return {5,10}
    # 숫자인 경우 None을 반환해서 별도 처리
    return None

a = input().strip()
b = input().strip()
c = input().strip()
tokens = [a,b,c]

# 숫자인지 확인
nums = [None, None, None]
for i,t in enumerate(tokens):
    if t not in ("Fizz","Buzz","FizzBuzz"):
        # 숫자라고 가정 (문제 보장)
        try:
            nums[i] = int(t)
        except:
            nums[i] = None

# 경우 1: 숫자가 하나라도 있으면 그 숫자를 기준으로 시작값 x 계산
found = False
for i,n in enumerate(nums):
    if n is not None:
        x = n - i  # tokens[i]는 x+i에 대응
        # x는 1 이상이어야 함 (문제의 i=1,2,...)
        if x >= 1:
            if fb(x) == a and fb(x+1) == b and fb(x+2) == c:
                print(fb(x+3))
                found = True
                break
# 경우 2: 숫자 없어서 모듈러로만 결정
if not found:
    rsets = [residues_for(t) for t in tokens]  # 각 위치의 가능한 mod15 집합
    # r0 후보 탐색 (0..14)
    for r0 in range(15):
        if r0 in rsets[0] and ((r0+1) % 15) in rsets[1] and ((r0+2) % 15) in rsets[2]:
            # 양수로 만들기: residue 0 -> 15, else 그대로 (작은 양수 해)
            if r0 == 0:
                x = 15
            else:
                x = r0
            print(fb(x+3))
            found = True
            break

# 안전망(문제 입력은 항상 유효하므로 여기까지 도달하지 않아야 함)
if not found:
    # fallback: brute force 큰 범위 (숫자가 큰 경우에도 안전하게)
    for x in range(1, 10**8 + 1):  # 숫자 길이 8 이하라 가정하면 충분
        if fb(x) == a and fb(x+1) == b and fb(x+2) == c:
            print(fb(x+3))
            found = True
            break
