s = int(input("Enter the no. of fresh loaves purchased: "))
e = int(input("Enter the no. of day old loaves purchased: "))
l = 185
print("Regular price: Rs. 185")
amtNew= s*l
amtOld = e*l
amtOldDis = amtOld *(6/10)
if (s<0):
    print ("Invalid input")
else:
    print("Amount of new loaves: ",amtNew)
    print("Amount of day old loaves: ",amtOldDis)
    print("Total Amount : ",amtNew + (amtOld-(amtOldDis)))
    
  
