#Part 1

def draw_stars(li):
	for i in range(len(li)):
		str = ""
		for num in range(li[i]):
			str += "*"
		print str


#Part 2

def draw_stars2(li):
	for i in range(len(li)):
		string = ""
		if type(li[i]) == str:
			word = li[i]
			for num in range(len(word)):
				string += word[0]
			print string.lower()
		elif type(li[i]) == int:
			for num in range(li[i]):
				string += "*"
			print string
