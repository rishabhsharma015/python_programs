a=int(input())
b=int(input())
k=min(a,b)
for i in range(k,0,-1):
	if a%i==0 and b%i==0:
		break
print("H.C.F is --",i)


