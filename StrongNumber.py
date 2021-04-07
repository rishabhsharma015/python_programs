import math as m
n = int(input("Enter the number: "))
s = str(n)
sum = 0
for i in s:
    sum = sum + m.factorial(int(i))
print("Strong") if(sum == n) else print("Not Strong")