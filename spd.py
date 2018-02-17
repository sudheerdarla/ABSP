#! python3

'''
This is the program to find the strongest password
with min 8 characters
min one digit
including both upper and lower case
'''

import re

text1 = input('''(Requirements: 
- Minimum 8 characters.
- Atleast one digit.
- Atleast one UPPERCASE
- Atleast one lowercase.)
Enter your password: ''')

minDigitRegex = re.compile(r'\d+?')
digilist = minDigitRegex.findall(text1)

uppers = [l for l in text1 if l.isupper()]       # list comprahension

lowers = [l for l in text1 if l.islower()]


# foo = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

def spd():
	if len(text1) >= 8:
		if len(digilist) != 0:
			if len(uppers) != 0:
				if len(lowers) != 0:
					print(text1)

spd()