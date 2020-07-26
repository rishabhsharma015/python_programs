l1=[]
l=list(map(int,input().split()))
for i in l:
	for j in l:
		k=i^j
		l1.append(k)
l1.sort()
t=l1.pop()
print(t)
