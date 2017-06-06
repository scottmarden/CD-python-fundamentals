def type_test(var):
	if type(var) == str:
		if len(var) >= 50:
			print "Long sentence"
		else:
			print "Short sentence"
	elif type(var) == int:
		if var >= 100:
			print "That's a big number!"
		else:
			print "That's a small number"
	elif type(var) == list:
		if len(var) >= 10:
			print "Big list!"
		else:
			print "Short list"
