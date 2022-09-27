def maxProfit(price, s):
 
    
    profit = [0]*s
    Maximum_Price = price[s-1]
 
    for i in range(s-2, 0, -1):
 
        if price[i] > Maximum_Price:
            Maximum_Price = price[i]
 

        profit[i] = max(profit[i+1], Maximum_Price - price[i])
 
    Minimum_Price = price[0]
 
    for i in range(1, s):
 
        if price[i] < Minimum_Price:
            Minimum_Price = price[i]
 
        profit[i] = max(profit[i-1], profit[i]+(price[i]-Minimum_Price))
 
    result = profit[s-1]
 
    return result
 
 

price = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    sel = int(input())
    price.append(sel)
print(price) 
print ("Maximum profit is", maxProfit(price, len(price)))

