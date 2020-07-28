# In this, we are finding three highest values from a dictionary. 

d={}
l1=list(map(str,input().split()))
for i in l1:
	d[i]=int(input())
	d.update({i:d[i]})
print(d)
l=list(d.values())
l.sort()
c=1
print("The 3 highest values are-->")
while c<4:
	max=l.pop()
	print(max)
	c+=1


	
