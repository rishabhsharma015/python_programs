s = input("Enter the String in lower case: ")
s1 = ""
for i in range(len(s)):
    if s[i]!=" ":
        s1 = s1 + chr(ord(s[i]) - 32)
    else:
        s1 = s1 + " "
print("Output Upper String: "+s1)




