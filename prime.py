#just playing with list and list comprehension
print("Following are the prime numbers")
for i in range(1,25):
	#checking whether the value is greater than 1
	if i > 1:
		#below is just for iterating the i - range
		for n in range(2,i):
			if (i % n) == 0:
					break
		else:
			print (i)

