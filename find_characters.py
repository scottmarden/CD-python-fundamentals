def find_characters(li, val):
	new_li = []

	for word in li:
		if (word.find(val) != -1):
			new_li.append(word)
		else:
			continue
	print new_li

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

find_characters(word_list, char)
