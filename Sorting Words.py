Selmiya =[]
s= int(input("Enter the number of elements you want to print : "))
l= str(input("Order (A/D): "))
for i in range(s):
    e= str(input(" "))
    Selmiya.append(e)
Selmiya.sort()
if (l == 'A'):
    for sel in Selmiya:
        print(sel)
else:
    Selmiya.sort(reverse=True)
    for sel in Selmiya:
        print(sel)
    
