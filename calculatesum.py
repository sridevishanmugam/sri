
n1=int(input())
l1=list(map(int,input().split()))
c1=0
for i in range(0,n1):
    for j in range(0,i):
        if l1[j]<l1[i]:
            c1=c1+l1[j]
print(c1)
