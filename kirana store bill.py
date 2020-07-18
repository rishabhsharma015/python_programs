c=0
d=[]
e=[]
k=[]
l=['Yes','yes','y','Y','YES']
while(True):
	g=input("Enter item name: ")
	n=input("Enter item price: ")
	if n!='q' and g!='':
		c=c+int(n)
		d.append(g)
		e.append(n)
		
	else:
		print("Thanks for Shopping!!")
		print(f"Your total is - {c}")
		break
k=list(zip(d,e))
#print(k)

print("Do you want a Shopping bill--")
s=input()
if s in l:
	print(21*' ',end=' ')
	print("SHRIRAM GENERAL STORE")
	print(14*' ',end=' ')
	print(34*'.')
	print(26*' ',end=' ')
	print("BILL RECIPT")
	print(14*' ',end=' ')
	print(34*'.')
for i in k:
	
	print(20*' ',end=' ')
	print(i[0],end=' ')
	print(12*' ',end=' ')
	print("Rs.",i[1])
print(14*' ',end=' ')
print(34*'.')
print(33*' ',end=' ')
print("Total : ",c)

	
		

	