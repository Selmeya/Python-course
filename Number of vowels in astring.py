s = input("Enter the sentence or word: ")
vowels='aeiou'
count= 0
for i in s:
    if i in vowels:
        count+=1
print('The number of vowels in',s,'is',count)
