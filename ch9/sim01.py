#! python3
# sim01.py - Walks a directory tree and archive just files with 
# certain extensions, such as .txt or .py and nothing else

import os, zipfile

def testBackup(folder):

	# make sure the path will be absolute path
	folder1 = os.path.abspath(folder)
	
	# create a zip folder in write mode
	backupZip = zipfile.ZipFile('testbackup.zip', 'w')

	# walk throgh the files and folders with os.walk method
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			# look for the filenames ends with .py or .txt
			if filename.endswith(('.py', '.txt')):
				#print(filename)
				# write/add that those files to zip file created
				backupZip.write(os.path.join(foldername, filename))

testBackup('test')