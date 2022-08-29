math=int(input("Enter the mark obtained in Mathematics:"))
eng=int(input("Enter the mark obtained in English :"))
comp=int(input("Enter the marks obtained in Computer Science:"))
phy=int(input("Enter the mark obtained in Physics:"))
chem=int(input("Enter the mark obtained in Chemistry:"))
 
total=(math+eng+comp+phy+chem)
print("Total marks obtained is:",total)
percentage=(((math+eng+comp+phy+chem)/500)*100)
print("Percentage :",percentage)
if percentage<=50:
    print("Grade is C")
elif percentage ==50 <<80:
    print("Grade is B")
elif percentage >80:
    print("Grade is A")
elif percentage ==80:
    print("Grade is A")
else:
    print("Failed")
# I. SELMEYA - 192121137 (BTECH - INFORMATION TECHNOLOGY)
    
