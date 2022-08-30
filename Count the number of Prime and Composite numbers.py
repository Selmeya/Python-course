p=0
c=0
n=int(input("enter a number: "))
if(n>0):
    for i in range(2,n+1):
        if(i%2!=0):
            p=p+1
        else:
            c=c+1
print("count of prime numbers",p)
print("count of composite numbers",c)
print("0 and 1 is neither prime nor composite")
