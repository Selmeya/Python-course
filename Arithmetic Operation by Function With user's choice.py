def Add(s,e):
    return s+e
def Sub(s,e):
    return s-e
def Pow(s,e):
    return s**e
def Mul(s,e):
    return s*e
def Div(s,e):
    return s/e
s = int (input("Enter any number 1: "))
e= int(input("Enter any number 2: "))
add= s+e
sub=s-e
powe=s**e
mul=s*e
div=s/e
print('div=s/e')
print('add= s+e')
print('sub=s-e')
print('powe=s**e')
print('mul=s*e')
print('div=s/e')
Choice =input("Enter the operation you want to do: ")
if (Choice == 'add'):
    print('Addition = {0}'.format(Add(s,e)))
elif( Choice == 'sub'):
    print('Subtraction = {0}'.format(Sub(s,e)))
elif(Choice =='powe'):
    print('Power ={0}'.format(Pow(s,e)))
elif(Choice == 'mul'):
    print('Multiplication = {0}'.format(Mul(s,e)))
elif(Choice=='div'):
    print('Division={0}'.format(Div(s,e)))
else:
    print('Invalid')
