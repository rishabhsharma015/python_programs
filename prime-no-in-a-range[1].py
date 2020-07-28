a=int(input("Enter lower limit"))
b=int(input("Enter upper limit"))
for i in range(a+1,b+1):
	for j in range(2,i+1):
		if i%j==0:
			break
			
	if i==j:
		print(i)
		

			
		