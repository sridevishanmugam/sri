m2,n2=map(str,input().split())
y2=0
if len(m2)>len(n2):
	m2,n2=n2,m2
p1=0
while p1<len(m2):
	  y2+=(ord(n2[p1])-ord(m2[p1]))
	  p1+=1
for p1 in range(p1,len(n2)):
	  y2+=ord(n1[p1])-ord('a')+1
print(y2)
