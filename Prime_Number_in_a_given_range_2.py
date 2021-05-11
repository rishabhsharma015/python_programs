# Printing Prime numbers in a given range

def isPrime(num):
    for i in range(2, num):
        if num%i==0:
            break

    else:
        print(num,end=" ")
a = int(input("Enter the lower bound: "))
b = int(input("Enter the upper bound: "))

for i in range(a, b+1):
    if(i!=1):
        isPrime(i)


