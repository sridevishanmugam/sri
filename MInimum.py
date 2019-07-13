from itertools import combinations
n,k2=map(int,input().split())
a2=len(str(n))
lst1=list(combinations(str(n),a2-k2))
lst1=sorted(lst1)
print(*lst1[0],sep='')
