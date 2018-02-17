from itertools import chain
from collections import defaultdict
dict1 = {'bookA': 1, 'bookB': 2, 'bookC': 3}
dict2 = {'bookC': 2, 'bookD': 4, 'bookE': 5}
dict3 = defaultdict(list)
for k, v in chain(dict1.items(), dict2.items()):
    dict3[k].append(v)

for k, v in dict3.items():
    print(k, v)
    if len([k]) > 1:
    	print(sum(dict3[k]))
    	dict3[k] = sum(v)

print(dict3)
print(sum(dict3[k]))