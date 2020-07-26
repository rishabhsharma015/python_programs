# maximum Xor.
l1=[]
l=list(map(int,input().split()))   # list of integer
for i in l:
	for j in l:
		k=i^j          # claculating the xor of elements
		l1.append(k)
l1.sort()
t=l1.pop()
print(t)
