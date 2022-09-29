def FactorialnFactor(n):
    if(n==1):
        return 1
    else:
        return n*FactorialnFactor(n-1)
try:
    s=int(input("Enter the number:"))
    if(s<=0):
        print("Invalid Input")
    else:
        print("Factorial:",FactorialnFactor(s))
        c=0
        for i in range(1,s+1):
            if(s%i==0):
                c+=1
        print("Number of factors:",c)
except ValueError:
    print("Invalid Input")
