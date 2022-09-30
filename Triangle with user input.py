Value= str(input("Enter the Character to be printed: "))
Rows= int(input("Enter the number of rows : "))
if (Rows <= 0):
    print("Invalid Input")
for i in range (Rows):
    for j in range  (i+1):
        print(Value,end=" ")
    print("\n")

