n=int(input("Enter the four digit number:"))
k=str(n)
s=k[0:2]
h=0
for i in s:
	h=h+int(i)
t=k[2:4]
g=0
for i in t:
	g=g+int(i)
if g==h:
	print("lucky number")
else:
	print("Not lucky number")
	

	
	
