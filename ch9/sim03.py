#!python3
# sim03.py is to find the folder in a directory tree that
# has the greatest number of files or the folder that uses
# most disk space

import os, operator

bigf = {}

totalsize = 0
for foldername, subfolders, filenames in os.walk('.'):
	for sub in subfolders:
		absp = os.path.abspath(sub)
		for a,b,c in os.walk(absp):
			relp = os.path.relpath(a)
			# loop throgh the list of files in a subfolder and 
			# add that filesize size to the to 'totalsize' and store it
			# with key value pair in 'bigf' dictionary.
			for i in c:
				totalsize += os.path.getsize(os.path.join(a, i))
				bigf[relp] = totalsize
		totalsize = 0

# just print created dict to check the values.
print(bigf)
# to get the key with hihgest value.
print("'" + max(bigf, key=bigf.get) + "'" + 'is the biggest subfolder!')

