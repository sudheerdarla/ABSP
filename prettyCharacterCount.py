import pprint

message = 'It was a bright cold dau in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count)