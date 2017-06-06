#Odd/Even - a function that counts from 1 to 2000. As loop executes, program prints the number of that iteration and specify whether it's odd or even.

def odd_even(start, end):
	for num in range(start, end):
		if num % 2 != 0:
			print "Number is " + str(num) + ". This is an odd number"
		else:
			print "Number is " + str(num) + ". This is an even number"


#Multiply - a function that iterates through each value in a list and returns a list where each value has been multiplied by 5.

def multiply(li, factor):
	for i in range(len(li)):
		li[i] *= factor
	print li
	return li

#Hacker Challenge -

def layered_multiples(arr):
	for i in range(len(arr)): #work through initial array
		new_arr = [] #create an array we can put the 1's into
		for num in range(arr[i]): #fill new array with 1's based on length of current arr index
			new_arr += [1]
		arr[i] = new_arr #set current arr index to our newly populated arrays of 1.
	return arr #give it back
