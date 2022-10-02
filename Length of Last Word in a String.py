def length(sel):
    count = 0
    flag= False
    length = len(sel)-1;
    while(length!=0):
        if(sel[length] == ' '):
            return count
        else:
            count+=1
        length-=1
    return count
sel = str(input("Enter a string: "))
print(length(sel))
