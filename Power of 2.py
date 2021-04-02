# my method to check whether a number is power of 2 or not
i=0
n=int(input("Enter the positive integer:"))

if n==1:
	print("Yes power of 2")
elif (n%2!=0):
	print("Not a power of 2")
elif (n%2==0):
	while ((2**i)!=n):
		i=i+1
		if (((2**i)%2==0 and (2**i) > n)):
			print("Not a power of 2")
			break
	if ((2**i)==n):
		print("Yes power of 2")
		print("power is : ",i)


	
