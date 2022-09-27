from collections import deque
def letterCombinationsUtil(Number, n, Table):
 
    list = []
    a = deque()
    a.append("")
 
    while len(a) != 0:
        s = a.pop()
 
        
        if len(s) == n:
            list.append(s)
        else:
 
           
            for letter in Table[Number[len(s)]]:
                a.append(s + letter)
 
    
    return list
 
 

def letterCombinations(Number, n):
 
    
    Table = ["0", "1", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]
 
    list = letterCombinationsUtil(Number, n, Table)
 
    s = ""
    for word in list:
        s += word + " "
    return s


Number = []
e = int(input("Enter number of elements : "))
for i in range(0,e):
    sel = int(input())
    Number.append(sel)
print(Number)

n = len(Number)

print(letterCombinations(Number, n))
