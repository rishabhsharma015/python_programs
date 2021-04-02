s = input()
for i in s:
	if i==' ':
		k=s.count(i)
		s=s.replace(i,'',k)
		break
print(s)
