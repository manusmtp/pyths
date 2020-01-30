#pgm for findall method of re and others

import re
#search matches the first match while findall is as the name indicated
#as there is no other group it returns all the matched string as list

print("enter any string emphasizing the regu.exp ex(343-2425)")
str2=input()

phoneR=re.compile(r'\d{3}-\d{4}')

mat1=phoneR.findall(str2)

for i in mat1:
	print("matched expression in group::",i)