def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return(n*factorial(n-1))
num=int(input("Enter any number: "))
print('number:',num)
print('Factorial:',factorial(num))
#I.Selmeya-192121137
