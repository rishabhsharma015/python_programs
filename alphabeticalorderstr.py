n=input("Enter the String: ")
k=list(n)
k.sort(reverse=False)
s=''.join(map(str,k))
print("String characters in sorted order: ",s)

