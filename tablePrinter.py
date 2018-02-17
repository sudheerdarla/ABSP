tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

maxWidths = []
for i in tableData:
	maxWidths.append(len(max(i, key=len)))
print(maxWidths)

def printTable(data):
	for i in range(len(tableData[0])):
		lst2 = [item[i].rjust(maxWidths[0], ' ') for item in tableData]
		print(' '.join(lst2))

printTable(tableData)
