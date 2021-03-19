a = int(input())
k=2
l=[]
while(a>0):
	for i in range(2,k+1):
		if k%i==0:
			break
		
	if i==k:
		l.append(k)
		a-=1
	k+=1
print(l[-1])

