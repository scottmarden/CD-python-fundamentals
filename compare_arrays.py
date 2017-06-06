def compare_lists(list_one, list_two):

	equal = 1

	if len(list_one) == len(list_two):

		i = 0
		while (i < len(list_one)):
			if list_one[i] != list_two[i]:
				equal = 0
				break
			else:
				i += 1

	else:
		equal = 0

	if (equal == 1):
		print "The lists are the same"
	else:
		print "The lists are not the same."

list_one = ['celery','carrots','bread']
list_two = ['celery','carrots','bread']


compare_lists(list_one, list_two)
