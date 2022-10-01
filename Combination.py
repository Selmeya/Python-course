Selmiya=[]
s= int(input("Number of elements in a list: "))
for l in range(0,s):
    e=int(input(" "))
    Selmiya.append(e)
print(Selmiya)
    

for i in range(0,s):
   for j in range(0,s):
      for k in range(0,s):
         if(i!=j&j!=k&k!=i):
            print(Selmiya[i],Selmiya[j],Selmiya[k])
