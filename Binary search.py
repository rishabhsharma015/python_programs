l=list(map(int,input("Enter array element-").split()))
print("Sorted array-")
for i in range(1,len(l)):
	for j in range(0,len(l)-i):
		if l[j]>l[j+1]:
			t=l[j]
			l[j]=l[j+1]
			l[j+1]=t
print(l)
item=int(input("Enter the element to search-"))
low=0
up=len(l)-1
while low<=up:
	m=(low+up)//2
	if l[m]==item:
		print("Search successful")
		print("At an index %d",m)
		break
	elif l[m]<item:
		low=m+1
	else:
		up=m-1
	