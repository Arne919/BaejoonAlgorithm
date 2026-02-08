import sys
s,p=map(int, sys.stdin.readline().split())
arr=list(sys.stdin.readline().rstrip())
a,c,g,t=map(int,sys.stdin.readline().split()) #A,C,G,T 개수 조건

answer=0
base_arr=arr[0:p] #첫 시작을 위해 직접 구간 설정.

#첫번째는 직접 구간 설정해서 개수 세기
a_cnt=c_cnt=g_cnt=t_cnt=0
for char in base_arr:
        if char=='A':
            a_cnt+=1
        elif char=='C':
            c_cnt+=1
        elif char=='G':
            g_cnt+=1
        elif char=='T':
            t_cnt+=1

#조건 체크
if a_cnt>=a and c_cnt>=c and g_cnt>=g and t_cnt>=t:
        answer+=1


#첫번째 이후는 슬라이딩을 통해 개수 +,- 하기
for i in range(s-p): #첫번째 이후 (s-p)번 반복함 (자명한 사실)
    getOut=arr[i]
    getIn=arr[i+p]

    #슬라이딩으로 인해 나가는 놈
    if getOut=='A':
            a_cnt-=1
    elif getOut=='C':
            c_cnt-=1
    elif getOut=='G':
            g_cnt-=1
    elif getOut=='T':
            t_cnt-=1

    #슬라이딩으로 인해 들어오는 놈
    if getIn=='A':
            a_cnt+=1
    elif getIn=='C':
            c_cnt+=1
    elif getIn=='G':
            g_cnt+=1
    elif getIn=='T':
            t_cnt+=1

    #조건 체크
    if a_cnt>=a and c_cnt>=c and g_cnt>=g and t_cnt>=t:
        answer+=1
    
print(answer)