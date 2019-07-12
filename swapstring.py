s1=input()
s1=list(s1)
res=""
for i in range(0,len(s1)-1,2):
  temp=s1[i+1]
  s1[i+1]=s1[i]
  s1[i]=temp
print(res.join(s1))
