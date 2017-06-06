odd_line = "* * * * "
even_line = " * * * *"

line = 1

while (line < 9):
	if line % 2 != 0:
		print odd_line
		line += 1
	else:
		print even_line
		line += 1
