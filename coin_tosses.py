def coin_toss():
	import random
	attempts = 0
	h = 0
	t = 0
	while attempts <= 5000:
		toss = round(random.random())
		if toss == 0:
			h += 1
			print "Attempt #" + str(attempts) + ": Throwing a coin....It's a head! ... Got " + str(h) + " head(s) so far and " + str(t) + " tail(s) so far"
		elif toss == 1:
			t += 1
			print "Attempt #" + str(attempts) + ": Throwing a coin....It's a head! ... Got " + str(h) + " head(s) so far and " + str(t) + " tail(s) so far"
		attempts += 1
