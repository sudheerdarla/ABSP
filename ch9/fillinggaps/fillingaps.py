import os, re

def filling(folder):
	abspath = os.path.abspath(folder)
	pattern = re.compile(r'\d{1,}')
	numlist = []
	for foldername, subfolder, filenames in os.walk(abspath):
		for filename in filenames:
			if filename.startswith('spam00'):
				mo = pattern.search(filename)
				num = int(mo.group())
				numlist.append(num)
			numlist.sort()
		print(numlist)
		original_list = [x for x in range(numlist[0], numlist[-1] + 1)]
		print(original_list)
		numlist = set(numlist)
		print(numlist)
		missed_list = (list(numlist ^ set(original_list)))
		print('Missed files are: ', missed_list)
		print('And they had been created, please check the files! :)')

		for i in range(len(missed_list)):
			newfile = 'spam00' + str(missed_list[i]) + '.txt'
			open(newfile, 'w')
			# print(newfile)

filling('.')