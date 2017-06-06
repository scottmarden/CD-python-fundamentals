import turtle

DIST = 100
for x in range(0,20):
		print "x", x
		for y in range(1,5):
			print "y", y
			turtle.right(45)
			turtle.forward(DIST)
		DIST += 20

DIST = 100
for x in range(0,10):
		print "x", x
		for y in range(1,5):
			print "y", y
			turtle.right(45)
			turtle.forward(DIST)
		DIST += 20

DIST = 100
for x in range(0,8):
		print "x", x
		for y in range(1,5):
			print "y", y
			turtle.right(120)
			turtle.forward(DIST)
		DIST += 20
