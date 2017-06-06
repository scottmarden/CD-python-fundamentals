prime_count = 0

for num in range (100, 100001):

	prime = "false"
	square = "false"


	if (num**.5 % 1) == 0:
		square = "true"

	elif num % 2 == 0:
		prime = "false"
	else:
		for div in range (3, num/2):
			if num % div == 0:
				prime = "false"
				break
			else:
				prime = "true"


	if prime == "true":
		print "Foo"
		prime_count += 1

	elif square == "true":
		print "Bar"

	else:
		print "Foobar"

print prime_count
