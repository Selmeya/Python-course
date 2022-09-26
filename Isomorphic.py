s = str (input("s = " ))
e = str (input("t= "))
def isIsomorphic (s,e):
    dict_s={}
    dict_e={}
    for i, value in enumerate (s):
        dict_s[value] = dict_s.get(value,[])+[i]
    for j, value in enumerate (e):
        dict_e[value]=dict_e.get(value,[])+[j]
    if sorted(dict_s.values())== sorted(dict_e.values()):
        return True
    else:
        return False
print(isIsomorphic(s,e));
        
