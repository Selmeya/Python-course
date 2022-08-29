def fibonacci_recur(n):
    if(n<=1):
        return 1
    else:
        return(fibonacci_recur(n-1)+fibonacci_recur(n-2))
num=int(input("Enter the nth number: "))
print('Fibonacci Sequence: ')
for i in range(num):
    print(fibonacci_recur(i))
    #I.Selmeya - 192121137
