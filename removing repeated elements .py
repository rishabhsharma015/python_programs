l=list(map(int,input("Enter the elements-->").split()))
print("List with repeated elements",l)
k=[]
for i in l:
	if i not in k:
		k.append(i)
print("Repeated elements Removed",k)

