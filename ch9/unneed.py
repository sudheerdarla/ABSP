#!python3
# unneed.py - walks through the filenames and prints the 
# files and its sizes which are greater than '1Mb'.

import os

def unneed(folder):
	abspath = os.path.abspath(folder)
	print('Files which are greater than 1 MB:')
	for foldername, subfolder, filenames in os.walk(abspath):
		for filename in filenames:
			filesize = os.path.getsize(os.path.join(foldername, filename))
			if filesize > 1000000:
				print(filename, '(', round(filesize/1000000, 2),'MB)')

unneed('.')