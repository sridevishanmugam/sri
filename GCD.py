import math
p1,q1=map(int,input().split())
r1=[]
s1=list(map(int,input().split()))
for i in range(0,q1):
    u1,v1=map(int,input().split())
    r1.append([u1,v1])
for i in r1:
    x1=i[0]-1
    y1=i[1]-1
    print(math.gcd(s1[x1],s1[y1]))
