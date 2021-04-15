a=int(input("Enter a=="))
b=int(input("Enter b=="))
c=int(input("Enter c=="))
D=(b**2)-(4*a*c)
if D>0:
	print("The roots are real and distinct")
	x1=(-b+(D**0.5))/(2*a)
	x2=(-b-(D**0.5))/(2*a)
	print(round(x1,1))
	print(round(x2,1))

elif D<0:
	print("The roots are imagnery")

elif D==0:
	print("The roots are real and equal")
	x1=(-b+(D**0.5))/(2*a)
	x2=(-b-(D**0.5))/(2*a)
	print(round(x1,1))
	print(round(x2,1))
	
	
    
    