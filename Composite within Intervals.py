Lower=int(input("A= "))
Upper=int(input("B= "))
if (Lower== Upper):
    print("None")
elif(Upper<=0):
    print("Invalid input")
elif(Upper<=Lower):
     print("Invalid input")
    
for s in range (Lower+1,Upper+1):
    factor = 0
    for i in range(1,s+1):
        if(s%i==0):
            factor+=1

    if (factor>2):
        print(i)
