c=0
l1=list(map(str,input().split()))
l2=list(map(str,input().split()))
for i in l1:
	for j in l2:
			if sorted(i)==sorted(j):
				c=c+1
print(c)

