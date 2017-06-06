column = 1

while column <= 12:

	row = 1
	rowStr = ""

	while row <= 12:
		rowStr +=" " + str(row*column)
		row += 1

	print rowStr
	column += 1
