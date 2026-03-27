mn, mx = map(int,input().split())

cnt = mx-mn+1
memo = [True] * (mx-mn + 1)

#제곱수들의 배수들을 cnt에서 빼줌
for i in range(2,int(mx**0.5)+1):
    for j in range((mn//(i*i))*(i*i),mx+1,i*i):
        if j-mn >= 0 and memo[j-mn]: #이미 판단했던 값(memo가 False)이면 넘기기
            cnt -= 1
            memo[j-mn] = False
print(cnt)