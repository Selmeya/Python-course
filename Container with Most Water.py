def MaxArea(S, Len) :
    Area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
           

            Area = max(Area, min(S[j], S[i]) * (j - i))
    return Area
 
s = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    sel = int(input())
    s.append(sel)
print(s)
len1 = len(s)
print(MaxArea(s, len1))
