def items(s):
    e=200*(s-1)
    return e
l=int(input("Enter the number:"))
if(l>=0):
    print("Number of items:",l)
    print("Shipping charge:",items(l)+750)
else:
    print("Invalid Input")
