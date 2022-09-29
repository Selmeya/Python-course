Selmiya=[]
s= int(input("Enter the number of elements: "))
for i in range(s):
    e=float(input())
    Selmiya.append(e)
print (Selmiya)
print(sorted(Selmiya))
def getMean(Selmiya):
    Selmiya.sort()
    Sum= 0
    for i in Selmiya:
        Sum +=i
        l= Sum/len(Selmiya)
    return round( l)
print("Mean: ",getMean(Selmiya))
def getMedian(Selmiya):
    Selmiya.sort()
    if len(Selmiya)%2!= 0:
        return Selmiya[len(Selmiya)//2]
    else:
        L1= Selmiya[len(Selmiya)//2]
        L2= Selmiya[len(Selmiya)//2-1]
        return ((L1 +L2)/2)
print("Median: ",getMedian(Selmiya))        
def getMode(Selmiya):
    mode = sorted(set(Selmiya),key= Selmiya.count,reverse = True)
    Max_Mode = Selmiya.count(mode[0])
    Result_Mode =[]
    for i in mode:
        if Selmiya.count(i)<Max_Mode:
            break
        Result_Mode.append(i)
    return sorted(Result_Mode)
print("Mode = ",getMode(Selmiya))
