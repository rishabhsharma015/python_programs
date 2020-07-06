s=input("Enter the sentence---")
b=[]
for i in s:
	if i not in b and i.isalpha():
		b.append(i)
if len(b)==26:
	print("Pangram")
else:
	print("Not Pangram")
	