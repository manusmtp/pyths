#list comprehension

import timeit
#timeit module describes the time it takes to complete the execution of code

s = [x ** 2 for x in range(10) ]
print s

#2 to the pwr , 2 to the power 3 , 2 to 4 
v = [2 ** i for i in range(10)]
print v

#x value existing in s and it should be even we have used the logic mod 2
#below one is quite elegant
#take each value from s : used for loop to break the : error , if for is not there , then compiler may rise the
#error
m = [x for x in s if x % 2 == 0 ]
print m

#list comprehension is very good alternative to repeatable for loops

# Initialize the `kilometer` list 
kilometer = [39.2, 36.5, 37.3, 37.8]
# Construct `feet` with `map()`
feet = map(lambda x: float(3280.8399)*x, kilometer)
# Print `feet` as a list 
print(list(feet))
#each value of x is coming from the list, which is mapped to the list

#checking the value of each item in list
#below code converts each value to string even though it is int, we are going to write same code without the manual conversion
list1= [2243,343,34,'2323',"A4343"]
for i in range(len(list1)):
	print ("%s type is %s"% (list1[i],type(str(i))))


list2= [2243,343,34,'2323',"A4343"]
for i in range(len(list2)):
	print ("%s type is %s"% (list2[i],type(i)))
