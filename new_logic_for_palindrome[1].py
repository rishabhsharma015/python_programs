s=input()
c=0
for i in range(len(s)):
	if s[i]==s[len(s)-1-i]:
		c=c+1	
		
if c==len(s):
	print("palindrome")
else:
	print("Not palindrome")
