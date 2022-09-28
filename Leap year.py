Year=int(input("Enter the year: "))
if (Year %400 == 0) and (Year % 100):
    print(Year,'is a leap year')
elif(Year<0):
    print("Invalid input")
elif(Year%4==0)and (Year%100!=0):
    print(Year,'is a leap year')

else:
    print(Year,'is not a leap year')
