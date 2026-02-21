n = int(input())
count =1
towers = list(map(int,input().split()))

for i in range(n-1):
    if towers[i] <=  towers[i+1]:
        count +=1
print(count)