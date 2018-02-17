# catNames = []

# while True:
# 	print('Enter the name of cat' + str(len(catNames) + 1) + 
# 		'(Or enter nothign to stop.):')
# 	name = input()
# 	if name == '':
# 		break
# 	catNames = catNames + [name] # list concatination
# print('the cat names are:')
# for name in catNames:
# 	print(' ' + name)
spam = ['hello', 'howdy', 'hello']
for i in spam:
	if i == 'hello':
		print(spam.index(i))
