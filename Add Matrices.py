s=int(input("Enter number of rows in Matrix1:"))
e=int(input("Enter number of columns in Matrix1:"))
l=[]
for i in range(s):
    m=[]
    for j in range(e):
        y=int(input("Enter element Matrix1 :"))
        m.append(y)
    l.append(m)
s1=int(input("Enter number of rows in Matrix2:"))
e1=int(input("Enter number of columns in Matrix2:"))
l1=[]
for i in range(s1):
    m1=[]
    for j in range(e1):
        y1=int(input("Enter element Matrix2 :"))
        m1.append(y1)
    l1.append(m1)
print("MATRIX 1:")
for i in range(s):
    for j in range(e):
        print(l[i][j],end=" ")
    print()
print("MATRIX 2:")
for i in range(s1):
    for j in range(e1):
        print(l1[i][j],end=" ")
    print()
if(s!=s1 or e!=e1):
    print("Matrices with different number of columns and rows can not be added")
else:
    a=[]
    for i in range(s):
        a1=[]
        for j in range(e):
            n=l[i][j]+l1[i][j]
            a1.append(n)
        a.append(a1)
    print("Added matrix :")
    for i in range(s):
        for j in range(e):
            print(a[i][j],end=" ")
        print()
