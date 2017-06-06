#Find and Replace

words = "It's thanksgiving day. It's my birthday, too!"

print words.find("day")

new_words = words.replace("day", "month")

print newWords


#Min and Max

x = [2,52,-2,7,12,98]

min = min(x)

max = max(x)

print min
print max


#First and Last

y = ["hello",2,52,-2,7,12,98,"world"]

first = y[0]
last = y[len(y)-1]

print first
print last


#New List

a_list = [19,2,54,-2,7,12,98,32,10,-3,6]

a_list.sort()

new_list1 = []

new_list2 = []

for i in range(len(a_list)/2):
	new_list1.append(a_list[i])

for i in range(len(a_list)/2, len(a_list)):
	new_list2.append(a_list[i])

new_list2.insert(0, new_list1)
