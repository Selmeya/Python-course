Selmiya = str(input("Enter a string "))
print("Vowels in ", Selmiya,"are : ")
for ch in Selmiya:
    if ch in "AEIOUaeiou":
        print(ch,end= " ' ")
print("\nConsonants in ", Selmiya,"are : ")
for ch in Selmiya:
    if ch not in "AEIOUaeiou":
        print(ch,end= " ' ")

