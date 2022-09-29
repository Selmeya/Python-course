s=int(input("Enter length of array:"))
l=[]
e=[]
for i in range(0,s):
    m=input("Enter the string")
    l.append(m)
for i in range(0,s):
    y=len(l[i].split())
    e.append(y)
print("LIST =",l)
print("Maximum  words in a string =",max(e))
