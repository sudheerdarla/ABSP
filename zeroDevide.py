def spam(devideBy):
	try:
		return 34 / devideBy
	except ZeroDivisionError:
		print('Error: Invalid argument.')

print(spam(2))
print(spam(4))
print(spam(0))
print(spam(6))