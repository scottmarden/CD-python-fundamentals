def make_dict(li1, li2):
	new_li = []
	for i in zip(li1, li2):
		print i
		new_li.append(i)
	print new_li
	new_dict = dict(new_li)
	print new_dict


name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]



make_dict(name, favorite_animal)
