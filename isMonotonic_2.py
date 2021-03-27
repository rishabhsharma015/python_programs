def isMonotonic(l):
    return (all(l[i]<=l[i+1] for i in range(len(l)-1)) or (all(l[i]>=l[i+1] for i in range(len(l)-1))))
List = list(map(int,input().split()))
print(isMonotonic(List))
