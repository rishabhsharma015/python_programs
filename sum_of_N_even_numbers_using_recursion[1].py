def f(N):
	if N==1:
		return 2
	else:
		return (2*N)+f(N-1)
k=f(int(input('Enter the number ')))
print(k)
