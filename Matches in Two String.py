def Match_Position(str1,str2):
	s=str1.replace('  ',' ')
	e=str2.replace('  ',' ')
	if(len(s)<len(e)):
		length=len(s)
	else:
		length=len(e)
	count=0
	for i in range(length):
		if(s[i]!=e[i]):
			count=count+1
	print(length-count)
str1=str(input("s1 = "))
str2=str(input("s2 = "))
Match_Position(str1,str2)
