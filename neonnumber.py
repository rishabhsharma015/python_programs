n=int(input("Enter the number -->"))
k=0
s=n**2
while s!=0:
	r=s%10
	k=k+r
	s=s//10
	
if k==n:
	print("Number is neon ")
else:
	print("Number is not neon")

	