import re

'''
this program is to play with regular expression
which follows same concepts as bash or unix regular expression
'''

print("Enter any US phone number ")
phone=input()
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d\d)')
ans=phoneRegex.search(phone)
if ans:
	print("there is a valid phone number enetered")
else:
	print("this is not a valid phone number")
#below one print the first three numbers if there is a match

#print(ans.group(1))

#another way to shorter the code using the below convention
secondPhone = re.compile(r'(\d{3})-\d{4}')
ans1=secondPhone.search(phone)
if ans1:
	print("there is match")
