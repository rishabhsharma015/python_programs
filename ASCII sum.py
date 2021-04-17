def outer(a,b):
	def inner():
		nonlocal a
		nonlocal b
		a=ord(a)
		b=ord(b)
	inner()
	return (a+b)
s=outer(input(), input())
print(s)
