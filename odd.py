print("Following the odd numbers")
for i in range(1,20):
	if i % 2 == 0:
		pass
	else:
		print(i)

print("Following are the even numbers")
for i in range(1,20):
	if i % 2 == 0:
		print(i)


print("sum of the digits from a given list")
nadd=[232,23,34,45,46,4,34,343,34,63,34]
count = 0
for i in range(0,len(nadd)):
	count += nadd[i]
print count

