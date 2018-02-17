import re

def stripReg(text, char):
	
	stripRegex = re.compile(r'\w+')
	stripStrip = stripRegex.findall(text)

	modified = re.sub(char, '', text)

	print("spaces removed spaces from both ends: " + stripStrip[0])
	print("removed the char the you want: " + modified)

inputText = input("Enter a string: ")
inputChar = input("Enter a char to be deleted: ")

stripReg(inputText, inputChar)


