a,b,c,d=map(int,input("Enter the four sides of rectangle: ").split())
l=[]
l.append(a)
l.append(b)
l.append(c)
l.append(d)
if l.count(a)==2 and l.count(b)==2 and l.count(c)==2 and l.count(d)==2:
	print('YES')
else:
	print('NO')
