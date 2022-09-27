s = (input("a =  "))
e = (input("b =  "))

def sum_ofBinary(s, e):
        max_len = max(len(s), len(e))
 
        s = s.zfill(max_len)
        e = e.zfill(max_len)
         
        result = ''

        carry = 0

        for i in range(max_len - 1, -1, -1):
            l = carry
            l += 1 if s[i] == '1' else 0
            l += 1 if e[i] == '1' else 0
            result = ('1' if l % 2 == 1 else '0') + result
            carry = 0 if l < 2 else 1 
         
        if carry !=0 : result = '1' + result
 
        return result.zfill(max_len)
if (s>='2' or s<='-1'):
    print("Invalid Input")
elif (e>='2' or e<='-1'):
    print("Invalid Input")
else:
    print(sum_ofBinary(s,e))


  
