#! python3
# madlibs.py - It read ine text files and lets user add their own text
# anywhere the words ADJECTIVE, NOUN, ADVERB or  VERB appears in a text file.

import re

# ask user for word inputs
adj = input("Enter an adjective: \n")
noun1 = input("Enter a noun: \n")
verb = input("Enter a verb: \n")
# noun2 = input("Enter a noun: \n")

# save the inputs in proper dictionary object
dic = {'ADJECTIVE': adj, 'NOUN': noun1, 'VERB': verb}

# open the text file and look for the words and replace them
# with user words accordingly.

# Open the text file with 'r+' :means both read and write access
spam = open('testtext.txt', 'r+')

# copy the text to other varable.
read_data = spam.read()

# function to iterate throgh dic and replace them in text file to print
def replace_all(read_data, dic):
    for i, j in dic.items():
        read_data = read_data.replace(i, j)
    print(read_data)

replace_all(read_data, dic)

spam.close()



#-----This a test to use if and else to find the solution------
# for i in range(len(foo)):
# 	if foo[i].upper() == 'ADJECTIVE':
# 		foo[i] = adj
# 	elif foo[i].upper() == 'NOUN':
# 		foo[i] = noun1
# 	elif foo[i].upper() == 'VERB':
# 		foo[i] = verb
# 	elif foo[i].upper() == 'NOUN':
# 		foo[i] = noun2

#-----This another test to use regex to find the solution------
# adjRegex = re.compile(r'ADJECTIVE \w+')
# test = adjRegex.sub(adj, read_data)
# print(test)
# nounRegex = re.compile(r'NOUN \w+')
# test = nounRegex.sub(noun1, read_data)
# print(test) 
# verbRegex = re.compile(r'VERB \w+')
# test = verbRegex.sub(verb, read_data)
