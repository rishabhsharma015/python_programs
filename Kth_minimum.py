list1 = list(map(int, input().split()))                       # Taking List as an input.
k = int(input())                                              # Taking k as input.
for i in range(0, k):
    m = list1[0]
    temp =0
    index = 0
    for j in range(0, len(list1)-i):
        if list1[j] <= m:
            m = list1[j]
            index = j
    temp = list1[index]                                        # Swapping two values.
    list1[index] = list1[len(list1)-1-i]
    list1[len(list1) - 1 - i] = temp

print(list1[len(list1)-k])
