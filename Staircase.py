def ways(n):
    if (n<=1):
        return n
    return ways(n-1)+ways(n-2)
s = int(input("n = "))
def countways(s):
    return ways(s+1)
print ( "Number of ways: ")
print(countways(s));
    
 
