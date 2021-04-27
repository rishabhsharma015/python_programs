n=int(input())
f=1
for i in range(n,0,-1):
	f=f*i
l=list(str(f))
for j in range(len(l)):
	k=int(l.pop())
	if k!=0:
		print("last non zero digit--",k)
		break
	
	
	
	
