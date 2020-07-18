from itertools import permutations
s=list(map(str,input().split()))
l=list(permutations(s))
d=[]

for i in l:
	c=0
	
	
	for j in range(1,len(i)):
		if i[j-1][-1]==i[j][0]:
			c+=1
			
	if c==len(i)-1:
		for j in i:
			d.append(j)
		break
		
d.append(d[0])
print(d)

