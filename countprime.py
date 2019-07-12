def prime(n):
  i=2
  while(i<n1):
    if n1%i==0:
        return false
    i=i+1
n1=input()
n1=n1.split()
i=int(n1[0])
j=int(n1[1])
count=0
while(i<=j):
    if(prime(i)):
      count+=1
    i=i+1
print(count)
