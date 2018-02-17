def printPicnic(itemsDict, leftWidth, rightWidth):
	print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
	print('Names'.center(leftWidth,' ') + 'V1'.rjust(rightWidth,' ') + 'V2'.rjust(rightWidth,' '))
	for k, v in itemsDict.items():
		print(k.ljust(leftWidth, '.') + str(v[0]).rjust(rightWidth) + str(v[1]).rjust(rightWidth))

picnicItems = {'sandiwiches': [4, 5], 'apples': [12, 13], 'cups': [4, 5], 'cookies': [800, 900]}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
