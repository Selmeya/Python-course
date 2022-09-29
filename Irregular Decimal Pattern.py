s=float(input("Enter the starting number: "))
e=int(input("Max number of line to be printed: "))
if(e<=0):
	print("Invalid Input")
	exit()
else:
    for i in range(1,e+1):
        for j in range(1,i+1):
            print("%.1f"%s,end=" ")
            s=s+0.1
        print("\n")
