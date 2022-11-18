s = int(input("Enter any number : " ))
sum = 0
l = s
while l>0:
    digit = l % 10
    sum+= digit**3
    l//=10
if s == sum:
    print(s, " is an Armstrong number" )
else:
    print(s," is not an Armstrong number")
