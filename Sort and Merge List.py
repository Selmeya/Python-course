s=int(input("Enter the length of list1:"))
l=[]
for i in range(s):
    e=int(input("Enter element :"))
    l.append(e)
m=int(input("Enter the length of list2:"))
y=[]
a=[]
for i in range(m):
    f=int(input("Enter element:"))
    y.append(f)
a=l+y
print("MERGED LIST :",sorted(a))
