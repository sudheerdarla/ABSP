'''---------------- Remove sensitive information such as 
Social Security or credit card numbers.---------------'''

import re

text = '''This the text tat includes credit card numbers, 
like 4587 2343 1234 4321 and 1234 4321 4567 7654, 
and more like 4567 7632 7896 1234, 1234-4321-1234-1234 so here i 
have to do is to hide the card numbers.. 
thats it for this task..hoohooo!'''
 
# create a regex to find all the CC numbers 
safeCreditRegex = re.compile(r'\d{4}[-.\s]\d{4}[-.\s]\d{4}[-.\s]\d{4}')
cardNumbers = safeCreditRegex.findall(text)

print(cardNumbers)
print(safeCreditRegex.sub('**** **** **** ****', text))
# replace those numbers with *'s

# display the text without numbers