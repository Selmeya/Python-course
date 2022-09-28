S = int(input("Enter the Principle Amount: "))
E = 10
L = int(input("Enter the Number of Years: "))
M = input("Is customer senior citizen(y/n): ")
def SimpleInterest(S,E,L,M):
    SI  = (S*E*L)/100
    if ( M == 'y'):
        E = 12
        print("The Simple Interest is ",SI)
    elif(S<0):
        print("Invalid Input" )
    elif(L<0):
        print("Invalid Input" )
    else:
        E = 10
        print("The Simple Interest is ",SI)

SimpleInterest(S,E,L,M)
    
