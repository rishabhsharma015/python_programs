s = input("Enter the String in Upper case: ")
s1 = ""
for i in range(len(s)):
    if s[i]!=" ":
        s1 = s1 + chr(ord(s[i]) + 32)
    else:
        s1 = s1 + " "
print("Output Lower String: "+s1)