l=list(map(int,input("Enter array element-").split()))
print("Sorted array-")
for i in range(1,len(l)):
	for j in range(0,len(l)-i):
		if l[j]>l[j+1]:
			t=l[j]
			l[j]=l[j+1]
			l[j+1]=t
print(l)
