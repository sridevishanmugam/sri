s1=int(input())
s1=list(str(s1))
s2=""
n=len(s1)
n1=n-1
if(n%2==0):
  n=len(s1)//2
else:
  n=len(s1)//2+1
for i in range(0,n):
  temp=s1[i]
  s1[i]=s1[n1-i]
  s1[n1-i]=temp
s2=s2.joijn(s1)
print(int(s2))
