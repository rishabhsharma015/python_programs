a=int(input())
l,l1=[],[]
c=0
for i in range(2,a+1):
	if a%i==0:
		for j in range(2,i+1):
			if i%j==0:
				break
		if j==i:
			l.append(i)
print(l)
for i in range(len(l)):
	while a%l[i]==0:
		c+=1
		a=a//l[i]
	l1.append(c)
	c=0
print(l1)
