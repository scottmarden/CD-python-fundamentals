#multiples part 1
#using a for loop to print all odd numbers from 1 to 1,000


for num in range(1000):
	if (num % 2 != 0):
		print num

#multiples part 2
#using a for loop to print all the multiples of 5 from 5 to 1,000,000

for num in range(5, 1000001, 5):
	print num

#sum list
#print the sum of all the values in the list: a=[1,2,5,10,255,3]

list_sum = 0

a = [1,2,5,10,255,3]

for i in a :
	list_sum = list_sum + i

print list_sum


#average list
#print the average of the values in the list: a=[1,2,5,10,255,3]

a = [1,2,5,10,255,3]

for i in a:
	sum = sum + i

avg = sum / len(a)

print avg
