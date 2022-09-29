from math import factorial
s = int(input("Enter a number of rows:"))
e=int(input("Enter the row number"))
if(s>0):
    for i in range(s):
        for j in range(s-i+1):
            print(end=" ")
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print()
    if(e>0):
        l=0
        for i in range(s):
            for j in range(i+1):
                if(i==e-1):
                    l+=factorial(i)//(factorial(j)*factorial(i-j))
        print("Sum of numbers:",l)
    else:
        print("INVALID INPUT")
else:
    print("INVALID INPUT")
