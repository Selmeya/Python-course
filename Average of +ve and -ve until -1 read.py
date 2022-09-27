print("Enter -1 to exit... ")
s=[]
e=[]
while True:
    l=int(input("Enter the number "))
    if(l==-1):
        break
    if(l>0):
        s.append(l)
    else:
        e.append(l)

Selmiya=(sum(s)/len(s))
Selmeya=(sum(e)/len(e))
print("The average of negative number is: ",Selmiya)
print("The average of positive number is: ",Selmeya)
