
findn = open("number2w", "r")


n = 10001
for num in findn.readlines() :
	splitn = num.split("_")
	if int(splitn[0]) == n :
		
		n += 1
		
	else:
		print n
		n += 2
	

findn.close()