def isMonotonic1(l):
    c = 0
    for i in range(len(l)-1):
        if(l[i]>=l[i+1]):
            c+=1
    if(c == (len(l)-1)):
        return True
    return False

def isMonotonic2(l):
    c = 0
    for i in range(len(l) - 1):
        if (l[i] <= l[i + 1]):
            c += 1
    if (c == (len(l) - 1)):
        return True
    return False
List = list(map(int,input().split()))
B = isMonotonic1(List)
if not(B):
    print(isMonotonic2(List))