n1=int(input())
st1=[]
for i in range(0,n1):
    s1=input()
    st1.append(s1)

i=0
count=0
f=True
for i in range(0,len(st1[0])):
    if(f==False):
        break
    j=1
    while(j<n1 and st1[0][i]==st1[j][i]):
        j+=1
    if(j==n1):
        count+=1
    else:
        f=False
        break
    
for i in range(0,count):
    print(st1[0][i],end="")
