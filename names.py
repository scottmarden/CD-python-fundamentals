# Part 1

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def names(li):
	for d in li:
		string = ""
		for key in d:
			string += " " + str(d[key])
		print string

names(students)

#Part 2

users = {
 	'Students': [
    	{'first_name':  'Michael', 'last_name' : 'Jordan'},
    	{'first_name' : 'John', 'last_name' : 'Rosales'},
    	{'first_name' : 'Mark', 'last_name' : 'Guillen'},
    	{'first_name' : 'KB', 'last_name' : 'Tonel'}
  	],
 	'Instructors': [
    	{'first_name' : 'Michael', 'last_name' : 'Choi'},
    	{'first_name' : 'Martin', 'last_name' : 'Puryear'}
  	]
 }

def more_names(dic):
	for li in dic:
		print li
		list_num = 1
		for sub_dic in dic[li]:
			name = ""
			nospace = ""
			for key in sub_dic:
				name += " " + sub_dic[key]
				nospace += sub_dic[key]
			print str(list_num) + " -" + name + " - " + str(len(nospace))
			list_num += 1

more_names(users)
