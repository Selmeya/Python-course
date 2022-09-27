Selmiya = []

s= int(input("Enter the number of elements you want to print in the list: "))
for i in range (1,s+1):
    sel = int(input("Enter the %d element : "%i))
    Selmiya.append(sel)
print(Selmiya)
Selmiya.sort()
print(Selmiya)

e = int(input("M = "))
if( e>=s+1):
         print("Invalid input")

Sum = Selmiya[e-1] +Selmiya[l-1]
Diff = Selmiya[l-1] -Selmiya[e-1]
if(l >=s+1):
         print("Invalid input")
selmiya = Selmiya.sort()
if(e == 1):
    print("The ", e ,"Maximum Value: ",Selmiya[-(e)])
    print("The Minimum Value : ",Selmiya[l-1])
    Sum = Selmiya[-(e)] +Selmiya[l-1]
    Diff = Selmiya[-(e)] - Selmiya[l-1]
    print("The sum of minimum and maximum number is ",Sum)
    print("The difference between minimum and maximum number is ",Diff)
else:
    print("The ", l ,"Maximum Value: ",Selmiya[e-l])
    print("The",e," Minimum Value : ",Selmiya[l-1])
    print("The sum of minimum and maximum number is ",Sum)
    print("The difference between minimum and maximum number is ",Diff)



