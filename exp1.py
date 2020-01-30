import re

print("Enter any sentence or string which has man or woman keyword")
str1=input()

#below re match zero or more wo*man
regexK=re.compile(r'Bat(wo)*man')
match1=regexK.search(str1)

#expects the Bat word in front
if match1:
	print("there is word match")

regexK1=re.compile(r'(bat(wo)?man)')
match2=regexK1.search(str1)

if match2:
	print("there is match in the expression")

#combininig two regular expressions
regexK2=re.compile(r'(bat(ma)+(wo)*man)')
match3=regexK2.search(str1)

if match3:
	print("this is another match with one or more")