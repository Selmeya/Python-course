s = int(input("Enter the lower case: "))
e = int(input("Enter the upper case: "))
for i in range(s,e+1):
    order = len(str(i))
    sum =0
    l=i
    while l >0:
        digit = l%10
        sum +=digit** order
        l//=10
    if i == sum:
        print(i)
