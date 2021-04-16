n=input("Enter the string :")
k=''
for i in n:
	if i not in k:
		k=k+str(i)
print(k)
