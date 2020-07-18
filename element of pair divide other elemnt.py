l=list(map(int,input().split()))
l.sort()
c=0
for i in l:
	for j in l:
		if j%i==0 and i!=j:
			print((i,j))
			c+=1
print(c)
 
	