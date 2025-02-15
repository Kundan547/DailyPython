dictionary = {1: "Geeks", 2: "For", 3: "Geeks"}

print("Dictionary: {}".format(dictionary))

if 1 in dictionary:
	print(dictionary[1])
else:
	print("{} is Absent".format(1))

if 5 in dictionary.keys():
	print(dictionary[5])
else:
	print("{} is Absent".format(5))
