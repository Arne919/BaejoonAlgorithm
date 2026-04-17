n = int(input())

cnt = 99
if n < 100 :
    print(n)
else:
    for i in range(100, n+1):
        num = str(i)
        gap = int(num[0]) - int(num[1])
        status = False
        for j in range(1,len(num)-1):
            if int(num[j]) - int(num[j+1]) != gap:
                status = False
                break
            else:

                status = True
        if status:
            cnt += 1
    print(cnt)