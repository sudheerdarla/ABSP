# go through the files on the current working directory
# add 'spam_' at the starting of every filename

import os, shutil

for filename in os.listdir('C:\\Users\\hi\\Documents\\absp\\ch9'):
	filename1 = 'spam_' + filename 
	print(filename, filename1)
	shutil.move(filename, filename1)
