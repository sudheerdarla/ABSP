#! python3
# regSearch.py is a program the opens all '.txt' files in a folder and 
# searched for any line that matches a user supplied regex.
# The results should be printed to the screen.

import os, re

testRegex = re.compile(r'\w+')

textLines = []
for file in os.listdir():
	if file.endswith(".txt"):
		f1 = open(file, 'r')
		textLines.append(f1.readlines()[0])
print(textLines)

mo = []
for i in range(len(textLines)):
	mo.append(testRegex.findall(textLines[i]))
print(mo)