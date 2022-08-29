num1=int(input("NUMBER 1= "))
num2=int(input("NUMBER 2 = "))
Add=num1+num2
Sub=num1-num2
Div=num1/num2
Mul=num1*num2
Select =(input("Enter the operation: "))
if(Select== 'Add'):
    print(num1,'+',num2,'=',Add)
elif(Select=='Sub'):
    print(num1,'-',num2,'=',Sub)
elif(Select=='Div'):
    print(num1,'/',num2,'=',Div)
elif(Select=='Mul'):
    print(num1,'X',num2,'=',Mul)
else:
    print('Invalid')

