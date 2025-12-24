import sys
input = sys.stdin.readline

N, s = input().split()
N = int(N)
A = input().strip()

# 1. 자릿수 비교
if N < len(A):
    print(-1)
    sys.exit()

if N > len(A):
    print(s.replace('?', '1'))
    sys.exit()

# 2. 같은 자릿수
coupon = list(s)
greater = False

for i in range(N):
    if greater:
        if coupon[i] == '?':
            coupon[i] = '1'
        continue

    if coupon[i] == '?':
        if A[i] == '0':
            coupon[i] = '1'
            greater = True
        else:
            coupon[i] = A[i]
    else:
        if coupon[i] < A[i]:
            print(-1)
            sys.exit()
        elif coupon[i] > A[i]:
            greater = True

print(''.join(coupon))
