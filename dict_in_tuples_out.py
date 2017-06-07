def dic_in_tup_out(dic):
	li = []
	for key in dic:
		tup = (key, dic[key])
		print tup
		li.append(tup)
	return li


my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

dic_in_tup_out(my_dict)
