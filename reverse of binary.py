def binrev(a):
	b2=str(bin(a)[2: : ])
	b3=int(str(bin(a)[2: : ])[-1: :-1])
	print("rev is",b3)
binrev(int(input()))
