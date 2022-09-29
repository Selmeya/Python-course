Rows=int(input("Enter the number of row:"))
if (Rows<=0 ):
     print("Enter the valid number of rows to be printed")
else:
    for i in range(Rows+1):
        for j in range(1,i+1):
            print(j/10,end=" ")
        print("\n")
