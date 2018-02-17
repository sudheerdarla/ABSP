#! python3
# selectiveco.py - Walks a directory tree and archive just files with 
# certain extensions, such as .pdf or .jpg and nothing else

import os, shutil

def selectivecopy(folder):
	abspath = os.path.abspath(folder)
	
	for foldername, subfolder, filenames in os.walk(abspath):
		for filename in filenames:
			if filename.endswith(('.pdf', '.jpg')):
				filepath = os.path.join(foldername, filename)
				shutil.copy(filepath, 'selected')

selectivecopy('.')