def type_list(li):
	sum = 0
	string = ""
	typeS = 0
	typeI = 0

	for i in li:
		if type(i) == str:
			string = string + " " +i
			typeS += 1
		elif type(i) == int:
			sum += i
			typeI += 1

	if typeS > 0 and typeI > 0:
		print "The array you entered is of mixed type"
		print "String: " + string
		print "Sum: ", sum
	elif typeS > 0 and typeI == 0:
		print "The array you entered is of string type"
		print "String: " + string
	elif typeS == 0 and typeI > 0:
		print "The array you entered is of integer type"
		print "Sum: ", sum

l = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

print "test_case1"
type_list(l)
print "test_case2"
type_list(l2)
print "test_case3"
type_list(l3)
