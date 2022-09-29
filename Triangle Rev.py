def Triangle(s):
    k=s-1
    for i in range(0,s+1):
        for j in range(0,k+1):
            print(end=" ")
        k=k-1
        for j in range(i,0,-1):
            print(j," ", end="")
        print()
s=float(input("Enter the number of rows:"))
if(s<=0 or int(s)!=s):
    print("INVALID INPUT")
else:
    Triangle(int(s))
