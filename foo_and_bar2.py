for num in range (100, 100001):

	prime = 0
	square = "false"

	if (num**.5 % 1) == 0:
		square = "true"

	elif num % 2 == 0:
		primeNum = "false"
	else:
		for div in range (3, num/2):
			if num % div == 0:
				# prime = "false"
				break
			else:
				prime += 1

	# if prime == "true":
	# 	print "Foo"
	#
	# elif square == "true":
	# 	print "Bar"
	#
	# else:
	# 	print "Foobar"

print prime
