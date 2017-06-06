my_dict = {"name":"Scott", "age":"31", "home country":"The United States", "favorite language":"Python"}

def bio(dict):
	for key in dict:
		print "My " + key + " is " + dict[key]
