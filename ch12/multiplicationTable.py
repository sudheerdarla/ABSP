#! python3
# multiplicationTable.py - takes a number N from the command line
# and creates an N×N multiplication table in an Excel spreadsheet.

# (not completed)

import openpyxl, sys

wb = openpyxl.Workbook()
sheet = wb.active

N = int(sys.argv[1])

for i in range(1, N+1):
	sheet['A' + str(i + 1)] = i
	# print(sheet['A' + str(i + 1)].value)

spam = {
	'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H',
	'9':'I', '10':'J', '11':'K'
}

j = 1
if j <= N:
	for rowOfCellObjects in sheet['B1': spam[str(N+1)] + '1']:
		for cellObj in rowOfCellObjects:
			cellObj.value = j
			j += 1
			# print(cellObj.coordinate, cellObj.value)

for i in range(1, N+1):
	sheet['B' + str(i + 1)] = '=SUM(A2:B1)'
	print(sheet['B' + str(i + 1)].value)

# for rowOfCellObjects in sheet['B2': spam[str(N+1)] + '1']:
# 	for cellObj in rowOfCellObjects:
# 		cellObj.value = '*'
# 		print(cellObj.coordinate, cellObj.value)

# wb.save('mul11.xlsx')