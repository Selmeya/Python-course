
def numberPalindrome(Number):
    for i in range(0,len(Number)//2):
        if (Number[i] != Number[len(Number)-i-1]):
            return False
    return True
Number = (input("Enter the number: "))
if(numberPalindrome(Number)== True):
    print(True)
else:
    print(False)
numberPalindrome(Number)
    
