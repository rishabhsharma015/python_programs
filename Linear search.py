l=list(map(int,input("Enter array element-").split()))
k=int(input("Enter the element to search"))
for i in l:
	if i==k:
		print("search successful")
		break
	else:
		print("Not in array")
		break

