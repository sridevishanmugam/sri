p1 = int(input())
q1 = list(map(int,input().split()))
c1 = 0
for i in range(p1):
    for j in range(i,p1):  
        for k in range(j,p1):
            if q1[i]<q1[j]<q1[k]:
                c1+=1
print(c1) 
