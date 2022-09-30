s=int(input("Enter value of X: "))
e=int(input("Enter value of N: "))
print("1=pow\n2=Add\n3=Sub\n4=Mul\n5=Div")
choice=int(input("Choice:"))
if (choice==1):
    pow=s**e
    print("Pow(%d,%d)=%d"%(s,e,pow))
elif (choice==2):
    add=s+e
    print("Add(%d,%d)=%d"%(s,e,add))
elif (choice==3):
    sub=s-e
    print("Sub(%d,%d)=%d"%(s,e,sub))
elif (choice==4):
    mul=s*e
    print("Mul(%d,%d)=%d"%(s,e,mul))
elif (choice==5):
    try:
        div=s/e
        print("Div(%d,%d)=%d"%(s,e,div))
    except ZeroDivisionError:
        print ("ZeroDivisionError")
else:
    print("Invalid Input...!")
