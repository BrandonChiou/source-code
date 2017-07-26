findn = open("number3w", "r")


n = 20001
k = 0
for num in findn.readlines() :
	splitn = num.split("_")
	if int(splitn[0]) == n :
		
		n += 1
		
	else:
		print n
		k += 1
		n += 2
	
print k
findn.close()