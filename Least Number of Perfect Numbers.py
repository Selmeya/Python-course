import sys
s = int(input("N = "))
def numSquares(s) :
    visited = [0]*(s + 1)
    e = []
    ans = sys.maxsize
    e.append([s, 0])    
    visited[s] = 1
    while(len(e) > 0) :
        l = e[0]
        e.pop(0)

        if(l[0] == 0) :
            ans = min(ans, l[1])
     
        i = 1
        while i * i <= l[0] :
            Path = l[0] - i * i
            if Path >= 0 and (visited[Path] == 0 or Path == 0) :

                visited[Path] = 1 

                e.append([Path,l[1] + 1])
             
            i += 1
    return ans
 
print(numSquares(s))
