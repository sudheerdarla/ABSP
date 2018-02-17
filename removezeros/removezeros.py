import re, os, shutil

for filename in os.listdir():
	# open('spam' + '00' + str(i) + '.txt', 'w')
	newFilename = re.sub('0+', '', filename)
	shutil.move(filename, newFilename)
