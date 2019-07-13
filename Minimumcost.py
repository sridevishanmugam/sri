a1,s1=input().split()
s2=abs(len(s1)-len(a1))
for i in range(len(a1)):
  if(len(s)==1 and s1[i] in a1):
    break
  if(a1[i]!=s1[i]):
    s2=s2+1
print(s2)
