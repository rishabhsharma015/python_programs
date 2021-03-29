def substringCount(s,sub):
    count = 0
    for i in range(len(s)):
        if (sub == s[i:len(sub) + i]):
            count += 1
    return count

s = input("Enter the String-->  ")
sub = input("Enter the substring-->  ")
print("Count of Substring is ",substringCount(s,sub))
